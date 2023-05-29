>> **Project Description -**

	1. Data is being dumped into ADSL Blob
	2. Created two folders 
		a. landing
		b. Processed - Processed CSV files are dumped (3 months)
	3. Self hosted Integration Runtime
	4. Linked Services for each component
	5. ADF Pipelines -
		a. Copy Data Activity
		b. For-each loop 
		c. Inside For each loop we have Databricks notebooks
			Data is already appended (Notebook will verify)
			Data is Appended 
		4. If output is 1 - Send mail to recheck
					2 - Send mail as Success
						Dump the csv into processed folder


					

>> What is Integration Runtime in ADF ?

	An integration runtime provides the bridge between activities and linked services. It's referenced by the linked service or activity, and provides the compute environment where the activity is either run directly or dispatched.

	1. AZURE Integration Runtime
	2. Self-Hosted Integration Runtime
	3. Azure SQL Server Integration Service (SSIS)

>> Differnet type of Triggers in ADF 

	Event Based
	Scheduled 
	Tumbling Window

>> Types of file formats in Azure

	Avro: 	Row Based
			Good for Transactional Work Loads

	Parquet: Coulmn Based
			 Good for Read Intensive Jobs like Analytical Workloads, Query Only Subset of a column,
			 Query Optimization Features

	ORC(Optimized Row Columnar): Similar to Parquet
								 Works well with analytical worklaods
								 Hive Competable
								 Enable ACID properties

	Atomicity - either the entire transaction takes place at once or doesn’t happen at all.
	Consistancy - integrity constraints must be maintained so that the database is consistent before and after the transaction
	Isolation - Transactions occur independently without interference.
	Durabality- once the transaction has completed execution, transactions are permanenet even for system failures


>> RDD vs DF - Which is Better and Why ?

	RDD - Collection of partitioned Data, No Built-in optimizer
	DF - Catalyst Optimizer. 

>> Onprem to Cloud data migration / ETL Components -
	
		Self-Hosted Integration Runtime
		Create Linked Services
		Create Copy- Activity
		Create a DataBricks Notebook for Data Transformation
		Output Data as Prquet Format and store it to Delta Table / 
			SQL Warehouse for BI Input

	

>> Security aspects of Azure Data Pipelines 
		
		Azure AD
		Key Vault for Storing Database or Other credentials
		Self hosted services , self hosted integration runtime
		encrypted file formats like AVRO or Parquet

>> Git

>> 	SCD 1: Data is overwritten, no History is Maintained
	SCD 2: History is Maintained in Differnet Rows , isActive = True / False, Using Version Number, Date Range
	SCD 3: Pirtial History is Maintained in an additaonal Column instead of an entire Row
	SCD 6: SCD1 + SCD2 + SCD3
			Additional Row with - isActive = True / False, Using Version Number, Date Range

>> Difference between WHERE and HAVING

	WHERE is Filtering Data from a Table query
	HAVING is Filtering Data from a Group / Group BY activity

>> Parameters in ADF:
	Parameters are basically used to make the ADF components dynamic rather than static. 

		1. Linked Service Parameters
		2. Dataset Parameters
		3. Pipeline Parameters
		4. Global Parameters

>> How to protect PII data during ingesion from on-prem to cloud usning Azure Data Engineering 

	To protect personally identifiable information (PII) data during ingestion from on-premises to the cloud using Azure Data Engineering, you can follow these best practices:

	1. Data Encryption
	2. Network Security (VPN) 
	3. Data Masking - Masking Sensetive Data in PII
	4. Role Based Access Control - to ensure that only authorized users have access to PII data. 
	5. Data Loss Prevention
	6. Data Retention and Purging 
	7. Data Monitoring


>> How you can move your changes from one environment to another environment for the Azure data factory?

	using the ARM template. ARM template is the JSON representation of the pipeline that we have created. Putting Eviornment details as dynamic variable, so we can deply each ARM templates in different environments just by changing the variables.

>> What are the two different types of execution modes provided by the Databricks?
	
	Interactive Mode:  In the interactive mode, you can run the code line by line and see the output. 

	Job Mode: In the job mode, it will run all code together, and then you will see the output.

>> What are the two different types of the cluster provided by the Databricks?

	Interactive Cluster: To run the interactive notebook you will be going to use an interactive cluster

	Job Cluster:  to run the job, we will use the job cluster

>> How many different types of cluster mode available in the Azure Databricks?

	Azure Databricks provides the three type of cluster mode :

	1. Standard Cluster: This is intended for single user. It can run workloads developed in any language: Python, R, Scala, and SQL.

	2. High Concurrency Cluster: A High Concurrency cluster is a managed cloud resource. It provide Apache Spark-native fine-grained sharing for maximum resource utilization and minimum query latencies. High Concurrency clusters work only for SQL, Python, and R. The performance and security of High Concurrency clusters is provided by running user code in separate processes, which is not possible in Scala.
	
	3. Single Node Cluster: A Single Node cluster has no workers and runs Spark jobs on the driver node. 

==================
ADF
==================

Very Important Question-
>> Question 1 : Assume that you are a data engineer for company ABC  The company wanted to do cloud migration from their on-premises to Microsoft Azure cloud.  You probably will use the Azure data factory for this purpose.  You have created a pipeline that copies data of one table from on-premises to Azure cloud. What are the necessary steps you need to take to ensure this pipeline will get executed successfully?

	STEP 1: The reason being the auto-resolve Integration runtime provided by the Azure data factory cannot connect to your on-premises.  Hence in step 1, we should create our own self-hosted integration runtime. Now this can be done in two ways:

		a. The first way is we can have one virtual Machine ready in the cloud and there we will install the integration runtime of our own.   

		b. The second way,  we could take a machine on the on-premises network and install the integration runtime there.

	STEP 2: Once we decided on the machine where integration runtime needs to be installed (let’s take the virtual machine approach). You need to follow these steps for Integration runtime installation.

		1. Go to the azure data factory portal. In the manage tab select the Integration runtime.

		2. Create self hosted integration runtime by simply giving general information like name description.

		3. Create Azure VM (If u already have then you can skip this step)

 		4. Download the integration runtime software on azure virtual machine. and install it.

		5. Copy the autogenerated key from step 2  and paste it newly installed integration runtime on azure vm.

	STEP 3: Once your Integration runtime is ready we go to linked service creation. Create the linked service which connect to the your data source and for this you use the integration runtime created above.

	STEP 4: After this we will create the pipeline.  Your pipeline will have copy activity where source should be the database available on the on-premises location. While sink would be the database available in the cloud.

	Once all of these done we execute the pipeline and this will be the one-time load as per the problem statement. This will successfully move the data from a table on on-premises database to the cloud database.

>> Question 2: Assume that you are working for a company ABC as a data engineer. You have successfully created a pipeline needed for migration. This is working fine in your development environment.  how would you deploy this pipeline in production without making any or very minimal  changes?

	we need to design our Azure data factory pipeline components in such a way that we can provide the environment related information dynamic and as a part of a parameter. There should be no hard coding of these kind of information.

	We need to create the arm template for our pipeline. ARM template needs to have a definition defined for all the constituents of the pipeline like Linked services, dataset, activities and pipeline.

	Once the ARM template is ready,  it should be checked-in into the GIT repository.  Lead or Admin will create the devops pipeline which will take up this arm template and parameter file as an input. Devops pipeline will deploy this arm template and create all the resources like linked service, dataset, activities and your data pipeline into the production environment.

>> Question 3: Assume that you have around 1 TB of data stored in Azure blob storage . This data is in multiple csv files. You are asked to do couple of transformations on this data as per business logic and needs,  before moving this data into the staging container.  How would you plan and architect the solution for this given scenario. Explain with the details.

	1. First of all, we need to analyze the situation. Here if you closely look at the size of the data, you find that it is very huge in the size. Hence directly doing the transformation on such a huge size of  data could be very cumbersome and time consuming process. Hence we should think about the big data processing mechanism where we can leverage the parallel and distributed computing advantages.. 

	Here we have two choices.

		a. We can use the Hadoop MapReduce through HDInsight capability for doing the transformation.

		b. We can also think of using the spark through the Azure databricks for doing the transformation on such a huge scale of data.
	
	Out of these two, Spark on Azure databricks is better choice because Spark is much faster than Hadoop due to in memory computation. So let’s choose the Azure databricks as the option.

	2.Next we need to create the pipeline in Azure data factory. A pipeline should use the databricks notebook as an activity.  

	We can write all the business related transformation logic into the Spark notebook. Notebook can be executed using either python, scala or java language. 

	When you execute the pipeline it will trigger the Azure databricks notebook and your analytics algorithm logic runs an do transformations as you defined into the Notebook. In the notebook itself, you can write the  logic to store the output into the blob storage Staging area.


	That’s how you can solve the problem statement.

>> Incremental Load ---

Question 4: Assume that you have an IoT device enabled on your vehicle. This device from the vehicle sends the data every hour and this is getting stored in a blob storage location in Microsoft  Azure. You have to move this data from this storage location into the SQL database.  How would design the solution explain with reason.

	This looks like an a typical incremental load scenario. As described in the problem statement, IoT device write the data to the location every hour. It is  most likely that this device is sending the JSON data to the cloud storage (as most of the IoT device generate the data in JSON format). It will probably writing the new JSON file every time whenever the data from the device sent to the cloud.

	Hence we will have couple of files available in the storage location generated on hourly basis and we need to pull these file into the azure sql database.

	we need to create the pipeline into the Azure data factory which should do the incremental load.  we can use the conventional high watermark file mechanism for solving this problem.

	Highwater mark design is as follows :

		1. Create a file named lets say HighWaterMark.txt and stored in some place in azure blob storage.  In this file we will put the start date and time.

		2. Now create the pipeline in the azure data factory.  Pipeline has the first activity defined as lookup activity. This will read the date from the HighWaterMark.txt

		3. Add a one more lookup activity which will return the current date time.

		4. Add the copy activity in the pipeline which will pull the file JSON files having created timestamp greater than High Water Mark date. In the sink push the read data into the azure sql database.

		5. After copy activity add the another copy activity which will update the current date time generated in the step 2, to the High Water Mark file.

		6. Add the trigger to execute this pipeline on hourly basis.

	That’s how we can design the incremental data load solution for the above described scenario.

>> 
