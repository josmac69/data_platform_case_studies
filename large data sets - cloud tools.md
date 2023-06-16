# Most commonly used tools for large data sets

## Data Transformation

Data transformation involves converting data from one format or structure into another. This is often necessary when moving data from one system to another, and can involve tasks like cleaning, aggregation, and integration. Here are a few tools and techniques that can be used for this purpose:

1. **Apache Hadoop**: Hadoop is an open-source software framework for storing data and running applications on clusters of commodity hardware. It provides massive storage for any kind of data, enormous processing power, and the ability to handle virtually limitless concurrent tasks or jobs. Hadoop uses MapReduce programming model for faster storage and retrieval of data.

2. **Apache Spark**: Spark is an open-source distributed computing system that can process large datasets in parallel. It's often used for tasks like data integration, cleaning, and transformation. Spark's in-memory processing capabilities make it faster than Hadoop for many tasks, and it also supports more flexible APIs.

3. **Apache Flink**: Flink is a stream processing framework that can run in all common cluster environments and perform computations at in-memory speed at any scale. It has robust capabilities for data transformation and integration.

4. **Google Cloud Dataflow**: This is a fully-managed service for transforming and enriching data in stream (real time) and batch (historical) modes with equal reliability and expressiveness.

5. **AWS Glue**: This is a fully managed extract, transform, and load (ETL) service that makes it easy to prepare and load your data for analytics.

## Data Analysis

Data analysis involves inspecting, cleaning, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making. Here are a few tools and techniques that can be used for this purpose:

1. **Apache Hive**: Hive is a data warehouse software project built on top of Apache Hadoop for providing data query and analysis. Hive gives an SQL-like interface to query data stored in various databases and file systems that integrate with Hadoop.

2. **Apache Pig**: Pig is a high-level platform for creating MapReduce programs used with Hadoop. The language for this platform is called Pig Latin. Pig Latin abstracts the programming from the Java MapReduce idiom into a notation which makes MapReduce programming high level, similar to that of SQL for RDBMS systems.

3. **Presto**: Presto is an open source distributed SQL query engine for running interactive analytic queries against data sources of all sizes ranging from gigabytes to petabytes.

4. **Google BigQuery**: BigQuery is Google's fully managed, NoOps, low-cost analytics database. With BigQuery you can query terabytes and terabytes of data without having any infrastructure to manage or needing a database administrator.

5. **Amazon Redshift**: Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. You can start with just a few hundred gigabytes of data and scale to a petabyte or more.

6. **Dask**: Dask is a flexible library for parallel computing in Python. It's often used in analytics where it can scale from single-machine to cluster-based computations.

7. **Apache Beam**: Beam is a model and set of language-specific SDKs for defining and executing data processing workflows, and also data ingestion and integration flows, supporting Enterprise Integration Patterns (EIPs) and Domain Specific Languages (DSLs).

Remember, the choice of tools depends on the specific requirements of your project, such as the size and type of your data, the processing power you have available, and the specific tasks you need to perform.