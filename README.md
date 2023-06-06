# Data platform - case studies

_**Still in progress, stay tuned!**_
<br>

## General notes
* So far investigation showed that Apache Spark is the most popular tool for processing of big data in data platforms
*

## Links to be reviewed
* [SnowPlow](https://github.com/snowplow/snowplow)
* [SeaTunnel](https://github.com/apache/seatunnel)
*

## Introduction
* In this repository I document my research of different existing DP / ETL solutions which are publicly available on GitHub
* I heavily utilized AI tools for this project - ChatGPT-4, ChatSonic and Github Copilot

## Reviewed projects
I will rate each project by stars (★☆☆☆☆ / ★★☆☆☆ / ★★★☆☆ / ★★★★☆ / ★★★★★) based on my opinion about the project after analyzing its code and documentation.
<br>

* [BDB - Unified integrated Data Analytics Platform](bdb/README.md) - ★★★★★
  *

* [Uber data platform](uber/README.md) - ★★★★★
  * This is a very interesting case study of Uber's data platform
  * It is not a GitHub project, but it is a very good source of information about data platforms
  * It is very well documented and it contains a lot of useful information
  * It is a very good starting point for learning about data platforms
<br>

* [Audiophile End-To-End ELT Pipeline](audiophile-end-to-end-elt-pipeline/README.md) - ★★★★☆
  * Pipeline scrapes data from Crinacle's website and stores them as CSV files in S3 bucket
  * Data are then loaded into Redshift and PostgreSQL databases
  * dbt is used for data transformation
  * The whole pipeline is orchestrated by Airflow
  * Highlights:
    * Repository has very mature Makefile which allows to easily build and run the pipeline
    * GitHub Actions are used for CI/CD
    * AWS resoureces are managed by Terraform
<br>

* [Finnhub Streaming Data Pipeline](finnhub-streaming-data-pipeline/README.md) - ★★★☆☆
  * This is a very interesting implementation of streaming data pipeline which uses Finnhub.io API/websocket to get real-time trading data
  * Data are scraped from websocket using python code and ingested into Kafka broker
  * Kafka is managed by Zookeeper and Kafdrop
  * Scala application running on Spark Kubernetes cluster is consuming data from Kafka and loads them into Cassandra tables
    * Repository contains Dockerfile showing how to build Cassandra image with setup `.cql` script, which creates Cassandra tables on startup
  * Grafana is used for visualization
    * Repository contains Dockerfile demonstrating how to build Grafana image with Cassandra plugin and predefined dashboards
  * All parts are containerized into Docker containers and orchestrated by Kubernetes, deploymend and infrastructure is managed by Terraform
<br>

* [Streamify](streamify/README.md) - ★★☆☆☆
  * Data pipeline with Kafka, Spark, dbt, Docker, Airflow, Terraform, GCP
  * Solution is just a show case, it is not running on kubernetes, it is build using virtual machines on GCP
  * Docker images are quite complex, containing also Google Cloud SDK
  * Looks like `dbt` tool is used for data transformation, which is actually not recommended by dbt documentation
  * `dbt` is implemented using airflow running in bash operator, which is also not the best practice
  * Looks like it is not possible to run the whole pipeline locally without GCP
  * Looks like there are some testing scripts in the repository, which are not used in the pipeline
<br>

* [Surfline Dashboard](surfline-dashboard/README.md) - ★★☆☆☆
  * Very simple example of ETL pipeline which extracts data from Surfline API and loads it into PostgreSQL database using python code in Airflow
  * More complex than Reddit ETL Pipeline but still very simple
<br>

* [Reddit ETL Pipeline](reddit-etl-pipeline/README.md) - ★☆☆☆☆
  * This is a very simple example of ETL pipeline which extracts data from Reddit API and loads it into AWS Redshift using python code in Airflow
  * AWS parts are terraformed.
<br>

## Learning resources

### Videos
* [YouTube video course - Data Engineering Project Portfolio](https://www.youtube.com/playlist?list=PLBJe2dFI4sgukOW6O0B-OVyX9c6fQKJ2N)
* [YouTube video course - Data Pipeline on AWS](https://www.youtube.com/playlist?list=PLBJe2dFI4sgt-9GR2j-rTeKtimE9pfqyt)
* [Stock Market Real-Time Data Analysis Using Kafka](https://www.youtube.com/watch?v=KerNf0NANMo)
* [Twitter Data Pipeline using Airflow for Beginners](https://www.youtube.com/watch?v=q8q3OFFfY6c)
* [Scrape Amazon Data using Python](https://www.youtube.com/watch?v=2hPCX-p_X8Q)

### Articles & repositories
* [How To Become a Data Engineer](https://github.com/adilkhash/Data-Engineering-HowTo)


