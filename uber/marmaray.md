# Marmaray - Uber's Generic Data Ingestion and Dispersal Framework
https://www.uber.com/en-DE/blog/marmaray-hadoop-ingestion-open-source/

**Overview:**
- Marmaray is Uber’s open source, general-purpose Apache Hadoop data ingestion and dispersal framework and library.
- It is a plug-in-based framework built on top of the Hadoop ecosystem.
- Marmaray ensures that all ingested raw data conforms to an appropriate source schema, maintaining a high level of quality so that analytical results are reliable.

**Architecture:**
- Marmaray connects a collection of systems and services to produce quality schematized data, ingest data from multiple data stores into Uber's Hadoop data lake, build pipelines to crunch and process the ingested data, and serve the processed results to an online data store.
- It uses Apache Spark for data processing due to its in-memory processing semantics, Resilient Distributed Datasets (RDDs), easy-to-use APIs, native fault tolerance capabilities, and lower latency than MapReduce.
- Marmaray's architecture includes several components such as DataConverters, WorkUnitCalculator, Metadata Manager, ForkOperator and ForkFunction, ISource and ISink, and AvroPayload.

**Typical Use Cases:**
- Uber Eats: Marmaray ingests raw data from Uber Eats orders into Hive, applies machine learning models to produce derived datasets of recommended restaurants, and disperses this data into a low-latency storage system like Cassandra for faster access.
- Uber Freight: Marmaray ingests external data covering recency, relevance, lane information, and mileage into Freight Services, helping Uber Freight's business scale quickly.

**Place in Uber's Data Pipeline:**
- Marmaray is envisioned within Uber as a pipeline connecting data from any source to any sink depending on customer preference.
- It consolidates Uber's ingestion pipelines into a single source-agnostic pipeline and codebase, making it more maintainable and resource-efficient.
- Marmaray also supports data deletion by leveraging the Hudi storage format, an open source library developed at Uber that manages storage of large analytical datasets.
- Uber is planning to onboard all its workflows onto Marmaray to simplify its overall data architecture and ensure scalability.