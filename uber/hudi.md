# Hudi (Hadoop Upserts anD Incremental)
https://www.uber.com/en-DE/blog/hoodie/

Hudi, short for Hadoop Upserts Deletes and Incremental, is an open-source incremental processing framework developed by Uber. It was designed to address the need for a high-efficiency, low-latency data pipeline. Here are the key features, architecture, and use cases:

**Key Features and Architecture:**

- **Storage:** Hudi organizes a dataset into a partitioned directory structure under a basepath, similar to a traditional Hive table. The dataset is broken up into partitions, which are directories containing data files for that partition. Each partition is uniquely identified by its partitionpath relative to the basepath. Within each partition, records are distributed into multiple data files. Each data file is identified by both a unique fileId and the commit that produced the file. In the case of updates, multiple data files can share the same fileId written at different commits.

- **Metadata:** Hudi maintains the metadata of all activity performed on the dataset as a timeline, which enables instantaneous views of the dataset. This is stored under a metadata directory in the basepath.

- **Index:** Hudi maintains an index to quickly map an incoming record key to a fileId if the record key is already present. Index implementation is pluggable and the following are the options currently available: Bloom filter stored in each data file footer and Apache HBase.

- **Optimization:** Hudi storage is optimized for HDFS usage patterns. Compaction is the critical operation to convert data from a write-optimized format to a scan-optimized format. Since the fundamental unit of parallelism for a compaction is rewriting a single fileId, Hudi ensures all data files are written out as HDFS block-sized files to balance compaction parallelism, query scan parallelism, and the total number of files in HDFS.

- **Ingest Path:** Hudi is a Spark library that is intended to be run as a streaming ingest job, and ingests data as mini-batches (typically on the order of one to two minutes). However, depending on latency requirements and resource negotiation time, the ingest jobs can also be run as scheduled tasks using Apache Oozie or Apache Airflow.

- **Query Path:** The commit meta timeline enables both a read-optimized view and a realtime view of the same data in HDFS; these views let the client choose between data latency and query execution time. Hudi provides these views with a custom InputFormat, and includes a Hive registration module which registers both these views as Hive metastore tables.

- **Incremental Processing:** As previously stated, modeled tables need to be processed and served in HDFS for HDFS to become the unified serving layer. Building low-latency modeled tables requires the ability to chain incremental processing of HDFS datasets. Since Hudi maintains metadata about commit times and file versions created for every commit, incremental changeset can be pulled from a Hudi-specific dataset within a start timestamp and an end timestamp.

**Typical Use Cases and Tasks in Uber Data Pipeline:**

- **Data Ingestion:** Hudi is used to ingest data into HDFS in a unified and configurable way. It updates raw Hadoop tables incrementally with a data latency of 10-15 minutes, allowing for fast access to source data.

- **Data Updates:** Hudi enables updates, inserts, and deletes existing Parquet data in Hadoop. Moreover, Hudi allows data users to incrementally pull out only changed data, significantly improving query efficiency and allowing for incremental updates of derived modeled tables.

- **Data Processing:** Hudi's incremental processing capabilities make it ideal for use cases where complex joins or significant data crunching is needed at near real-time latencies. It enables stream-to-stream joins with watermarks and stream-to-dataset joins to compute and upsert modeled tables in HDFS.

-

Hudi, short for Hadoop Upserts Deletes and Incremental, is an open-source incremental processing framework developed by Uber. It was designed to address the need for a high-efficiency, low-latency data pipeline. Here are the key features, architecture, and use cases:

**Key Features and Architecture:**

- **Storage:** Hudi organizes a dataset into a partitioned directory structure under a basepath, similar to a traditional Hive table. The dataset is broken up into partitions, which are directories containing data files for that partition. Each partition is uniquely identified by its partitionpath relative to the basepath. Within each partition, records are distributed into multiple data files. Each data file is identified by both a unique fileId and the commit that produced the file. In the case of updates, multiple data files can share the same fileId written at different commits.

- **Metadata:** Hudi maintains the metadata of all activity performed on the dataset as a timeline, which enables instantaneous views of the dataset. This is stored under a metadata directory in the basepath.

- **Index:** Hudi maintains an index to quickly map an incoming record key to a fileId if the record key is already present. Index implementation is pluggable and the following are the options currently available: Bloom filter stored in each data file footer and Apache HBase.

- **Optimization:** Hudi storage is optimized for HDFS usage patterns. Compaction is the critical operation to convert data from a write-optimized format to a scan-optimized format. Since the fundamental unit of parallelism for a compaction is rewriting a single fileId, Hudi ensures all data files are written out as HDFS block-sized files to balance compaction parallelism, query scan parallelism, and the total number of files in HDFS.

- **Ingest Path:** Hudi is a Spark library that is intended to be run as a streaming ingest job, and ingests data as mini-batches (typically on the order of one to two minutes). However, depending on latency requirements and resource negotiation time, the ingest jobs can also be run as scheduled tasks using Apache Oozie or Apache Airflow.

- **Query Path:** The commit meta timeline enables both a read-optimized view and a realtime view of the same data in HDFS; these views let the client choose between data latency and query execution time. Hudi provides these views with a custom InputFormat, and includes a Hive registration module which registers both these views as Hive metastore tables.

- **Incremental Processing:** As previously stated, modeled tables need to be processed and served in HDFS for HDFS to become the unified serving layer. Building low-latency modeled tables requires the ability to chain incremental processing of HDFS datasets. Since Hudi maintains metadata about commit times and file versions created for every commit, incremental changeset can be pulled from a Hudi-specific dataset within a start timestamp and an end timestamp.

**Typical Use Cases and Tasks in Uber Data Pipeline:**

- **Data Ingestion:** Hudi is used to ingest data into HDFS in a unified and configurable way. It updates raw Hadoop tables incrementally with a data latency of 10-15 minutes, allowing for fast access to source data.

- **Data Updates:** Hudi enables updates, inserts, and deletes existing Parquet data in Hadoop. Moreover, Hudi allows data users to incrementally pull out only changed data, significantly improving query efficiency and allowing for incremental updates of derived modeled tables.

- **Data Processing:** Hudi's incremental processing capabilities make it ideal for use cases where complex joins or significant data crunching is needed at near real-time latencies. It enables stream-to-stream joins with watermarks and stream-to-dataset joins to compute and upsert modeled tables in HDFS.
