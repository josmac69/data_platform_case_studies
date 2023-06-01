# Streamify

## URL
https://github.com/ankurchavda/streamify

## Schema
(Downloaded from Streamify repository)
<img src="architecture.png" width=60% height=30%>

## Overview
The repository "Streamify" is a data engineering project that creates a data pipeline using various technologies. Here's a detailed summary:

**Objective**: The project streams events from a simulated music streaming service (similar to Spotify) and creates a data pipeline that consumes real-time data. The data includes events like a user listening to a song, navigating on the website, authenticating, etc. This data is processed in real-time and stored in a data lake periodically (every two minutes). An hourly batch job then consumes this data, applies transformations, and creates tables for a dashboard to generate analytics. The aim is to analyze metrics like popular songs, active users, user demographics, etc.

**Dataset**: The project uses Eventsim, a program that generates event data to replicate page requests for a fake music website. The results mimic real user data but are entirely synthetic. The song data is borrowed from the Million Songs Dataset.

**Tools & Technologies**:

- Cloud: Google Cloud Platform (GCP)
- Infrastructure as Code software: Terraform
- Containerization: Docker, Docker Compose
- Stream Processing: Kafka, Spark Streaming
- Orchestration: Airflow
- Transformation: dbt
- Data Lake: Google Cloud Storage
- Data Warehouse: BigQuery
- Data Visualization: Data Studio
- Language: Python

**Pros**:

1. The project uses a wide range of modern data engineering tools and technologies, making it a comprehensive solution for real-time data processing and analysis.
2. It includes a complete data pipeline from data generation to visualization, providing an end-to-end solution.
3. The use of Docker and Docker Compose ensures that the project is containerized and can be easily set up and run on any system.
4. The project uses Terraform for infrastructure as code, making the infrastructure setup repeatable and version-controlled.

**Cons**:

1. The project uses synthetic data, which may not reflect the complexities and challenges of dealing with real-world data.
2. The project currently does a full refresh of dimensions and facts instead of incremental updates, which could be inefficient for larger datasets.
3. The project lacks data quality tests, which are crucial for ensuring the accuracy and reliability of the data.
4. The project currently doesn't include CI/CD, which is essential for maintaining and updating the project in a production environment.

**Possible Improvements**:

1. Use managed infrastructure like Cloud Composer for Airflow and Confluent Cloud for Kafka.
2. Create a custom VPC network.
3. Build dimensions and facts incrementally instead of full refresh.
4. Write data quality tests.
5. Create dimensional models for additional business processes.
6. Include CI/CD.
7. Add more visualizations.

Please note that running this project on GCP will incur charges.