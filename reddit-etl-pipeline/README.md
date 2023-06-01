# Reddit ETL Pipeline

## URL
https://github.com/ABZ-Aaron/Reddit-API-Pipeline

## Schema

<img src="workflow.png" width=30% height=30%>

## Overview

* The GitHub repository is for a project titled "Reddit ETL Pipeline."
* This project is a data pipeline designed to extract data from the Data Engineering subreddit on Reddit.
* The output of this pipeline is a Google Data Studio report, which provides insights into the Data Engineering subreddit.

Here's a detailed breakdown of the architecture of this ETL data pipeline:

1. **Extract Data Using Reddit API**: The pipeline begins by extracting data from the Data Engineering subreddit using the Reddit API. This is the "Extract" part of the ETL process.

2. **Load into AWS S3**: After the data is extracted, it is loaded into AWS S3, a scalable storage service provided by Amazon Web Services. This is the "Load" part of the ETL process.

3. **Copy into AWS Redshift**: The data in AWS S3 is then copied into AWS Redshift, a data warehousing service that allows for fast querying and analysis of data.

4. **Transform Using dbt**: dbt (data build tool) is used to transform the data in Redshift. This is the "Transform" part of the ETL process. dbt allows for transformations to be defined as SQL select statements, making it a powerful tool for data transformation.

5. **Create PowerBI or Google Data Studio Dashboard**: After the data has been transformed, a dashboard is created using either PowerBI or Google Data Studio. This dashboard provides a visual representation of the data and allows for easy interpretation of the insights derived from the data.

6. **Orchestrate with Airflow in Docker**: The entire pipeline is orchestrated using Apache Airflow, a platform used to programmatically author, schedule, and monitor workflows. Airflow is run within Docker, a platform that allows for the packaging of applications and their dependencies into a standardized unit for software development.

7. **Create AWS Resources with Terraform**: Terraform, an open-source infrastructure as code software tool, is used to create and manage the AWS resources required for this pipeline.

The final output from this pipeline is a Google Data Studio report. The report is reading from a static CSV output from Redshift. The Redshift database was deleted after the data extraction to avoid incurring costs.

The repository also provides detailed setup instructions and notes on potential improvements.

**Pros of this solution**:

- Utilizes a wide range of tools, providing a comprehensive learning experience.
- The use of Docker and Airflow allows for efficient orchestration of the pipeline.
- The use of dbt for data transformation allows for transformations to be defined as SQL select statements, providing a lot of flexibility.
- The use of Terraform allows for easy creation and management of AWS resources.

**Cons of this solution**:

- The pipeline is more complex than necessary for the task at hand, which could lead to unnecessary complications.
- The Redshift database is deleted after data extraction, which means the data cannot be queried directly from Redshift after the pipeline has run.
- The pipeline may incur costs if not managed properly, particularly if large amounts of data are extracted or if the infrastructure is kept running for extended periods.

## Parts

* [Airflow](airflow.md)


## AI prompt

_Act as an expert on data engineering. Here I give you link to github repository. Please analyze content of this repository and give me a very detailed description of the architecture of this ETL data pipeline, its components, interactions between them and also discussion of pros and cons of this solutions. Here is the link - https://github.com/ABZ-Aaron/Reddit-API-Pipeline_
