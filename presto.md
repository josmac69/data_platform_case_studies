# Presto SQL Engine for Data Analytics and the Open Lakehouse

Presto is an open-source SQL query engine that is designed for fast, reliable, and efficient data analytics at scale. Here are the key features and use cases:

- **Alternative to Hadoop tools like Hive of Pig**: Presto was designed as an alternative to tools that query HDFS using pipelines of MapReduce jobs such as Hive or Pig, but Presto is not limited to accessing HDFS.
-
- **Fast and Reliable**: Presto is an in-memory distributed SQL engine, which makes it faster than other compute engines in the disaggregated stack. It is designed to run interactive/ad hoc queries at sub-second performance for high volume apps.

- **Scalable**: Presto can be used for interactive and batch workloads, small and large amounts of data, and scales from a few to thousands of users. It is used by some of the largest internet-scale companies, operating reliably at massive scales.

- **Federated Queries**: Presto can query relational & NoSQL databases, data warehouses, data lakes, and more. It has dozens of connectors available today, allowing querying data where it lives. A single Presto query can combine data from multiple sources, enabling analytics across an entire organization.

- **Standardized SQL**: With Presto, you get one familiar ANSI SQL language and one engine for your data analytics. This standardization means you don't need to switch to another lakehouse engine as your data needs evolve.

- **Open Source**: Presto is a neutrally governed open source project under The Linux Foundation. It can be run wherever you want, on-premises or in any cloud.

Typical use cases for Presto include:

- **Data Exploration**: Presto's ability to run interactive queries makes it ideal for exploring large datasets.

- **Data Analytics**: Presto is designed for high-performance analytics on large datasets, making it suitable for data scientists and analysts who need to run complex queries.

- **Data Federation**: Presto's ability to query data across multiple sources makes it a good choice for organizations that have data spread across different systems and want to analyze it in a unified way.

- **Data Lake Querying**: Presto can be used to query data stored in data lakes, enabling organizations to analyze large volumes of raw data.

- **Data Warehousing**: Presto can be used as a query engine for data stored in data warehouses, providing a scalable solution for running complex analytical queries.