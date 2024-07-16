# import os
import numpy as np
import pandas as pd
# import pendulum
import statsmodels.api as sm


from datetime import timedelta
from pathlib import Path
# from numpy import nan
from sklearn.cluster import Birch
from airflow.decorators import dag, task, task_group
from airflow.models import Variable
from airflow.utils.dates import days_ago
# from airflow.operators.empty import EmptyOperator
# from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from airflow_clickhouse_plugin.hooks.clickhouse_dbapi import ClickHouseDbApiHook
# from airflow.providers.smtp.hooks.smtp import SmtpHook
# from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['adey@fiskerinc.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

@dag(
    # schedule="0 0 * * 1,4",  # every Monday and Thursday at 00:00 PST
    # start_date=pendulum.datetime(2024, 1, 8, 11, tz="US/Pacific"),
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=["clickhouse", "azure"],
    default_args=default_args,
)

def brake_duration_model_with_vehicle_cluster():
    def execute_ch_query(query_name):
        dag_vars = Variable.get("brakeDurationModel", deserialize_json=True)
        ch_hook = ClickHouseDbApiHook(
            clickhouse_conn_id=dag_vars["clickhouse_conn_id"],
            database=dag_vars["ch_database"],
        )
        print("Testing Clickhouse connection...")
        print(ch_hook.test_connection())
        base_path = Path(__file__).parent
        query_path = (base_path / ('./sql/' + query_name + '.sql')).resolve()
        with open(query_path) as f:
            query = f.read().rstrip("\n")
        ch_hook.run(sql=query)

    @task()
    def create_feature_temp_table():
        execute_ch_query("create_feature_table_temp_shard")
        execute_ch_query("create_feature_table_temp")
    
    @task()
    def get_feature_temp_table_data():
        execute_ch_query("get_feature_table_temp_data")

    @task()
    def create_brake_duration_temp_table():
        execute_ch_query("create_brake_duration_table_shard")
        execute_ch_query("create_brake_duration_table")

    @task()
    def get_brake_duration_data():
        execute_ch_query("get_brake_duration_data")

    @task()
    def create_vehDF_table():
        execute_ch_query("create_vehDF_shard")
        execute_ch_query("create_vehDF")

    @task()
    def get_vehDF_data():
        execute_ch_query("get_vehDF_data")

    @task()
    def create_scr_lim_table():
        execute_ch_query("create_scr_lim_shard")
        execute_ch_query("create_scr_lim")

    @task()
    def analyze_final_data():
        dag_vars = Variable.get("brakeDurationModel", deserialize_json=True)
        ch_hook = ClickHouseDbApiHook(
            clickhouse_conn_id=dag_vars["clickhouse_conn_id"],
            database=dag_vars["ch_database"],
        )
        print("Testing Clickhouse connection...")
        print(ch_hook.test_connection())

        query = """
        select * from brake_duration_table
        """

        brake_duration = ch_hook.get_pandas_df(sql=query)

        new = brake_duration[['brake_duration', 'speed_applied', 'slip_avg']].reset_index(drop=True)
        new.sort_values(by=['brake_duration'], inplace=True)

        new['sm2_dur'] = new.iloc[:, 0].rolling(window=2).mean()
        #new['sm2_dur'] = new['brake_duration'].rolling(window=2).mean()
        new.dropna(inplace=True)
        
        exog = np.array(new.drop(['brake_duration', 'sm2_dur'], axis=1))
        endog = np.array(new['sm2_dur'])
        labels = np.array(new['brake_duration'])

        mod = sm.OLS(endog, exog)
        res = mod.fit()

        y_pred = res.predict(exog)
        #print((y_pred),(labels))

        error = y_pred - labels


        mape = 100 * abs(y_pred / labels - 1)
        accuracy = 100 - np.mean(mape)
        print("Accuracy: ", accuracy)

        error_df = pd.DataFrame(error)
        error_df.columns = ['error']

        cluster_df = pd.concat([error_df, new[['speed_applied']].reset_index(drop=True)], axis=1)

        model = Birch(threshold=0.01, n_clusters=3)
        model.fit(cluster_df)
        cluster_df['yhat'] = model.predict(cluster_df)
        #clusters = unique(cluster_df['yhat'])

        print("Parameter names of the regression model:")
        scr = new[['speed_applied', 'slip_avg', 'brake_duration']]
        scr['pred'] = round(res.params[0] * scr['speed_applied'] + res.params[1] * scr['slip_avg'],5)
        #print(scr)

        grouped = cluster_df.groupby('yhat').agg(
            min_speed_appl=('speed_applied', 'min'),
            max_speed_appl=('speed_applied', 'max'),
            avg_err=('error', 'mean'),
            std_err=('error', 'std')
        )
        # Round the aggregated values to 5 decimal places
        grouped = grouped.round({'min_speed_appl': 5, 'max_speed_appl': 5, 'avg_err': 5, 'std_err': 5})
        #print(grouped)

        #scr_lim = pd.merge(scr, grouped, how='outer', left_on='speed_applied', right_index=True)
        #scr_lim = scr_lim[(scr_lim['speed_applied'] <= scr_lim['max_speed_appl']) & (scr_lim['speed_applied'] >= scr_lim['min_speed_appl'])]

        scr_lim = pd.merge(scr, grouped, how='cross')
        scr_lim = scr_lim[
            (scr_lim['speed_applied'] <= scr_lim['max_speed_appl']) & 
            (scr_lim['speed_applied'] >= scr_lim['min_speed_appl'])
        ]

        scr_lim['lim_H'] = round(scr_lim['pred'] + scr_lim['avg_err'] + scr_lim['std_err'],5)
        scr_lim['lim_L'] = round(scr_lim['pred'] + scr_lim['avg_err'] - scr_lim['std_err'],5)
        scr_lim['flagged'] = np.where((scr_lim['brake_duration'] >= scr_lim['lim_L']) & (scr_lim['brake_duration'] <= scr_lim['lim_H']), 0, 1)
        #print(scr_lim)  # Uncomment this line if you want to print the final data

        data_tuples = list(scr_lim.itertuples(index=False, name=None))

        # Define the ClickHouse query for inserting data
        insert_query = f"INSERT INTO scr_lim VALUES"

        # Construct the query with data values
        insert_query += ", ".join(map(str, data_tuples))

        # Execute the query
        ch_hook.run(sql=insert_query)

    @task
    def update_ctrl_table():
        dag_vars = Variable.get("brakeDurationModel", deserialize_json=True)
        ch_hook = ClickHouseDbApiHook(
            clickhouse_conn_id=dag_vars["clickhouse_conn_id"],
            database=dag_vars["ch_database"],
        )
        print("Testing Clickhouse connection...")
        print(ch_hook.test_connection())
        query = f"DELETE from ctrl_table where VIN in (SELECT VIN from feature_table_temp)"
        ch_hook.run(sql=query)
        execute_ch_query("insert_new_vins_to_ctrl_table")


    @task(trigger_rule='one_failed')
    def delete_temp_tables():
        execute_ch_query("delete_feature_table_temp")


    create_feature_temp_table() >> get_feature_temp_table_data() >> \
    create_brake_duration_temp_table() >> get_brake_duration_data() >> \
    create_vehDF_table() >> get_vehDF_data() >> create_scr_lim_table() >> analyze_final_data()
    #>> update_ctrl_table() >> delete_temp_tables()

brake_duration_model_with_vehicle_cluster()