# Uber data platform

## URL
https://www.uber.com/en-DE/blog/uber-big-data-platform/

## Overview

Uber's data pipeline has evolved over the years as the scale of their operations has increased. As of 2018, Uber had over 100 petabytes of analytical data that needs to be processed and served with minimum latency through their Apache Hadoop® based Big Data platform.

### First Generation
Sure, here are the key points about the first generation of Uber's data pipeline:

- Before 2014, Uber's data could fit into a few traditional online transaction processing (OLTP) databases, specifically MySQL and PostgreSQL.
- Engineers had to access each database or table individually, and there was no global access or view of all stored data.
- The data was scattered across different OLTP databases, and the total data size was on the order of a few terabytes.
- As Uber's business grew, the amount of incoming data increased, necessitating the construction of the first generation of their analytical data warehouse.
- The goal of this warehouse was to make all analytical data accessible to analysts in one place.
- Uber categorized their data users into three main categories: city operations teams, data scientists and analysts, and engineering teams.
- They used Vertica as their data warehouse software due to its fast, scalable, and column-oriented design.
- They developed multiple ad hoc ETL (Extract, Transform, and Load) jobs that copied data from different sources into Vertica.
- To streamline data access, they standardized SQL as their solution's interface and built an online query service to accept user queries and submit them to the underlying query engine.
- This first generation data warehousing service was a huge success, providing users with a global view and access to all data in one place.
- However, this system had its limitations, such as data reliability concerns due to ad hoc ETL jobs and a lack of a formal schema communication mechanism.
- Scaling the data warehouse also became increasingly expensive, leading to the deletion of older, obsolete data to free up space for new data.

### Second Generation
- To address the limitations of the first generation, Uber re-architected their Big Data platform around the Hadoop ecosystem.
- They introduced a Hadoop data lake where all raw data was ingested from different online data stores only once and with no transformation during ingestion.
- They introduced Presto for interactive ad hoc user queries, Apache Spark for programmatic access to raw data, and Apache Hive for extremely large queries.
- All data modeling and transformation only happened in Hadoop, enabling fast backfilling and recovery when issues arose.
- Only the most critical modeled tables were transferred to their data warehouse, significantly lowering the operational cost of running a huge data warehouse.
- They leveraged the standard columnar file format of Apache Parquet, resulting in storage savings and compute resource gains.
- All data services in this ecosystem were made horizontally scalable, improving the efficiency and stability of their Big Data platform.
- They transitioned from JSON to Parquet to store schema and data together, building a central schema service to collect, store, and serve schemas.
- Fragile, ad hoc data ingestions jobs were replaced with a standard platform to transfer all source data in its original, nested format into the Hadoop data lake.
- With Uber’s business continuing to scale, they soon had tens of petabytes of data, with tens of terabytes of new data added to their data lake daily.
- However, they faced new challenges such as the massive amount of small files stored in their HDFS and data latency that was still far from what their business needed.
- The snapshot-based ingestion method was inefficient and prevented them from ingesting data with lower latency.
- ETL jobs that ingested data into the data warehouse were also very fragile due to the lack of a formal contract between the services producing the data and the downstream data consumers.
- The same data could be ingested multiple times if different users performed different transformations during ingestion, resulting in extra pressure on their upstream data sources and increased storage costs.
- Backfilling was very time-and-labor-consuming because the ETL jobs were ad hoc and source-dependent, and data projections and transformation were performed during ingestion.
- It was also difficult to ingest any new data sets and types due to the lack of standardization in their ingestion jobs.
