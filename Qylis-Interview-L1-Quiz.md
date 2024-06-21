1. Which of the following is NOT a valid method to persist data in a Spark DataFrame in PySpark?

    a. df.write.parquet("path/to/output")
    
    b. df.write.format("json").save("path/to/output")
    
    c. df.saveAsTable("table_name")
    
    d. df.writeText("path/to/output”)   `[Correct]`

2. In Apache Spark, which operation causes a shuffle?

    a. `filter`
    
    b. `map`
    
    c. `reduceByKey` [Correct]
    
    d. `flatMap`

3.  When working with Kafka in a Databricks notebook, which library is primarily used to read data from Kafka?

    a. `pyspark.streaming`
    
    b. `pyspark.sql.kafka` [Correct]
    
    c. `pyspark.sql.streaming`
    
    d. `pyspark.kafka`

4. How do you broadcast a small DataFrame to all worker nodes in PySpark?

    a. `df.broadcast()`
    
    b. `broadcast(df)` [Correct]
    
    c. `spark.broadcast(df)`
    
    d. `df.broadcast().to_nodes()`

5.  In Azure Data Lake Storage (ADLS), which of the following is a common way to authenticate and authorize access?

    a. Access Control Lists (ACLs) [Correct]
    
    b. Public-private key pairs
    
    c. Username and password
    
    d. API tokens

6. Which of the following is the correct way to start a structured streaming query in Spark to read from Kafka?

a.     spark.read.format("kafka").load()`

b. `spark.readStream.format("kafka").load()`  [Correct]

c. `spark.readStream.fromKafka().load()`

d. `spark.readStream.kafka("kafka").load()`

7. Which of the following PySpark transformations would you use to convert a DataFrame to a Delta Table?

a. `df.write.delta("path/to/delta_table")`

b. `df.write.format("delta").save("path/to/delta_table")`  [Correct]

c. `df.saveAsDelta("path/to/delta_table")`

d. `df.toDelta("path/to/delta_table")`

8. What does the `checkpoint` directory do in a Spark Streaming application?

a. Stores temporary data files

b. Saves the metadata and state information for fault tolerance [Correct]

c. Holds intermediate results

d. Contains logs of the streaming job

9.  How would you read a CSV file stored in Azure Data Lake Storage into a Spark DataFrame in Databricks using Python?

a. `spark.read.csv("adl://path/to/csv")`

b. `spark.read.format("csv").load("adl://path/to/csv")`

c. `spark.read.format("csv").option("path", "adl://path/to/csv").load()` [Correct]

d. `spark.read.option("format", "csv").load("adl://path/to/csv")`

10. In Spark, what is the purpose of the `repartition()` function?

a. Reduce the number of partitions in a DataFrame

b. Increase the number of partitions in a DataFrame

c. Shuffle data to create new partitions  [Correct]

d. All of the above

11. Which of the following is true about Azure Data Lake Storage (ADLS) Gen2?

a. It does not support hierarchical namespace

b. It integrates with Azure Blob Storage [Correct]

c. It is limited to 1 petabyte of data

d. It does not support Hadoop-compatible access

12.  How would you write a DataFrame to an S3 bucket in Parquet format in Databricks using Python?

a. `df.write.parquet("s3a://bucket/path")`

b. `df.write.format("parquet").save("s3a://bucket/path")`

c. `df.saveAsParquetFile("s3a://bucket/path")`

d. Both A and B. [Correct]

13. In Apache Kafka, what is a consumer group?

a. A set of brokers managing a topic

b. A set of producers sending data to a topic

c. A set of consumers coordinating to read data from a topic. [Correct]

d. A set of partitions within a topic

14. How do you enable checkpointing in a Spark Streaming application?
1 point

a. `streamingContext.checkpoint("path/to/checkpoint/dir")`

b. `streamingContext.setCheckpointDir("path/to/checkpoint/dir")`  [Correct]

c. `streamingContext.enableCheckpoint("path/to/checkpoint/dir")`

d. `streamingContext.checkpointDirectory("path/to/checkpoint/dir")`

15. Which of the following is NOT a valid Spark action ?

a. `collect()`

b. `count()`

c. `filter()`. [Correct]

d. `take(n)`

16. When using Azure Data Lake Storage with Databricks, which library is typically used to access ADLS Gen2?

a. `spark-adls-gen1`

b. `hadoop-azure-datalake`. [Correct]

c. `azure-datalake-gen2`

d. `hadoop-azure`


17.  What is the primary function of the `foreachBatch` method in Spark Structured Streaming?
1 point

a. To apply transformations to each micro-batch of data

b. To write each micro-batch to an external storage system [Correct]

c. To stop the streaming query after each batch

d. To process each micro-batch asynchronously

18. When writing a Spark application in Scala, what is the recommended approach for defining a schema for structured data?
1 point

a. Using Python dictionaries

b. Using custom data structures

c. Using Apache Spark SQL DataFrames

d. Using Java classes  [Correct]

19. When joining two large datasets in Spark, which technique is likely to be the most efficient for performance?
1 point

a. Using a nested loop to join each element

b. Using the join() transformation on DataFrames with a broadcast hash join strategy  [Correct]

c. Using a shuffle operation to combine datasets

d. All of the above

20. When designing a data pipeline in Spark, what is the trade-off between using wide transformations (like map()) and narrow transformations (like filter())?

a. Wide transformations are faster but require more memory.

b. Narrow transformations are faster but require more disk access. [Correct]

c. There is no significant difference in performance between wide and narrow transformations.

d. Wide transformations are always preferred for better performance.

21. You are working with a large dataset in Spark containing missing values. Which function is most suitable for handling missing values efficiently?

a. Using conditional statements within a map() transformation

b. Using the drop() transformation on an RDD to remove rows with missing values

c. Using the fillna() function on a DataFrame to impute missing values [Correct]

d. All of the above

22. When persisting a Spark DataFrame for future use, which storage level offers the best balance between performance and memory usage?

a. MEMORY_ONLY

b. MEMORY_AND_DISK   [Correct]

c. DISK_ONLY

d. The choice doesn't affect performance

23. You need to train a machine learning model using Spark MLlib. Which library is used to represent features and labels within the model?

a. Spark RDD

b. Spark DataFrame

c. Spark VectorAssembler  [Correct]

d. Spark SQL

24. In a Spark Streaming application, what happens to the state information when a worker node fails?

a. The entire streaming job needs to be restarted.

b. State information can be recovered from a checkpoint if enabled.  [Correct]

c. The state information is lost, leading to data inconsistencies.

d. Spark automatically replicates state information across worker nodes.

25.  What is the benefit of using Delta Lake tables in Databricks compared to traditional Apache Spark tables?

a. Faster data ingestion speeds

b. ACID transaction support for data consistency  [Correct]

c. Automatic data partitioning

d. All of the above

26.  You're designing a real-time anomaly detection pipeline for financial transactions. The data arrives in Apache Kafka streams. Which combination of technologies would be most efficient for processing and identifying anomalies?

a. Apache Spark Streaming with Spark SQL and statistical outlier detection algorithms. [Correct]

b. Apache Flink with custom anomaly detection functions written in Python.

c. Apache Kafka Streams API with pre-built anomaly detection libraries.

d. Azure Stream Analytics with built-in anomaly detection features.

27. Your Spark application is experiencing slow performance due to excessive shuffles during joins. How can you optimize the join operation for better efficiency?

a. Increase the number of partitions in your RDDs.

b. Use a broadcast join for smaller datasets involved in the join.

c. Implement custom partitioning logic based on join keys.

d. All of the above  [Correct]

28. You're building a recommendation engine for a large e-commerce platform using Spark MLlib. Which approach would be most suitable for modeling user-item interactions?

a. Logistic Regression

b. Collaborative Filtering techniques like Alternating Least Squares (ALS)  [Correct]

c. Support Vector Machines (SVM)

d. Random Forest

29. You're working with a large geospatial dataset in Spark containing latitude and longitude coordinates. Which library can be used to perform efficient spatial queries (e.g., finding nearby points)?

a. Spark SQL with built-in geospatial functions

b. Apache Geospatial Spark (GeoSpark)

c. Apache Sedona  [Correct]

d. Databricks Runtime with built-in geospatial support

30.  When working with sensitive data in Spark applications, what are some best practices for ensuring data security?

a. Use encryption at rest and in transit for data storage and transmission.

b. Grant minimal access permissions to users and applications.

c. Disable logging for Spark jobs to avoid sensitive data exposure.

d. All of the above  [Correct]

31. Which optimization technique in Spark can significantly reduce the amount of data shuffled during join operations?

a. Partition pruning

b. Caching

c. Broadcast joins  [Correct]

d. Coalescing

32.  How do you handle schema evolution in Delta Lake when new columns are added to the incoming data?

a. Use the `mergeSchema` option when writing data  [Correct]

b. Manually update the schema in the Delta table

c. Drop the Delta table and recreate it with the new schema

d. Use the `append` mode to automatically update the schema

33. In Kafka, what is the purpose of log compaction?

a. To delete old log segments

b. To reduce the disk space used by the logs

c. To ensure that the latest value for each key is retained  [Correct]

d. To replicate the logs to another Kafka cluster

34.  Which of the following is a valid way to specify the schema for a DataFrame when reading JSON data in PySpark?

a. `df = spark.read.schema(schema).json("path/to/json")`

b. `df = spark.read.option("schema", schema).json("path/to/json")`

c. `df = spark.read.format("json").schema(schema).load("path/to/json")`  [Correct]

d. Both A and C

35. What is the primary difference between `repartition` and `coalesce` in Spark?

a. `repartition` can increase the number of partitions, while `coalesce` can only decrease the number of partitions  [Correct]

b. `repartition` performs a full shuffle, while `coalesce` does not

c. `repartition` is used for RDDs, while `coalesce` is used for DataFrames

d. Both A and B

36. In Azure Databricks, which command is used to mount an Azure Data Lake Storage (ADLS) Gen2 account?

a. `dbutils.fs.mount(source = "adl://<storage-account-name>.dfs.core.windows.net/<filesystem>", mount_point = "/mnt/<mount-name>")`  [Correct]

b. `dbutils.fs.mount(source = "abfs://<filesystem>@<storage-account-name>.dfs.core.windows.net/", mount_point = "/mnt/<mount-name>")`

c. `dbutils.fs.mount(source = "wasbs://<container>@<storage-account-name>.blob.core.windows.net/", mount_point = "/mnt/<mount-name>")`

d. `dbutils.fs.mount(source = "adl2://<storage-account-name>.dfs.core.windows.net/<filesystem>", mount_point = "/mnt/<mount-name>")`

37. How can you achieve exactly-once semantics in Kafka when consuming and producing messages?

a. Enable idempotence on the producer and use Kafka Streams for processing  [Correct]

b. Use at-least-once delivery and handle duplicates in the consumer application

c. Use Kafka's `acks=0` setting to ensure messages are not lost

d. Use manual offsets management and commit offsets only after processing

38.  What is the role of the `spark.sql.shuffle.partitions` configuration in Spark?

a. To determine the number of partitions to use when shuffling data for joins or aggregations  [Correct]

b. To set the default number of partitions for DataFrames and Datasets

c. To configure the parallelism level of Spark SQL queries

d. To define the number of partitions for output files

39. In Spark Structured Streaming, which operation would you use to merge streaming data into an existing Delta Lake table with UPSERT semantics?

a. `mergeInto`

b. `upsert`

c. `merge`  [Correct]

d. `insertOrUpdate

40. In Databricks, how do you efficiently read a large Parquet file stored in ADLS Gen2 into a Spark DataFrame with predicate pushdown?

a. `df = spark.read.parquet("abfs://container@storage_account.dfs.core.windows.net/path/to/parquet").filter("column = 'value'")`

b. `df = spark.read.format("parquet").load("abfs://container@storage_account.dfs.core.windows.net/path/to/parquet").where("column = 'value'")`

c. `df = spark.read.format("parquet").option("pushdown", "true").load("abfs://container@storage_account.dfs.core.windows.net/path/to/parquet").filter("column = 'value'")`

d. `df = spark.read.format("parquet").option("predicatePushdown", "true").load("abfs://container@storage_account.dfs.core.windows.net/path/to/parquet").filter("column = 'value’”)`   [Correct]
