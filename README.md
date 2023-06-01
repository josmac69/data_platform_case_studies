# Data platform - case studies
* In this repository I document my research of different existing DP / ETL solutions which are publicly available on GitHub
* I heavily utilized AI tools for this project - ChatGPT-4, ChatSonic and Github Copilot

## Table of contents
I will rate each project by stars (★☆☆☆☆ / ★★☆☆☆ / ★★★☆☆ / ★★★★☆ / ★★★★★) based on my opinion about the project after analyzing its code and documentation.
<br>
* [Reddit ETL Pipeline](reddit-etl-pipeline/README.md) - ★☆☆☆☆
  * This is a very simple example of ETL pipeline which extracts data from Reddit API and loads it into AWS Redshift using python code in Airflow
  * AWS parts are terraformed.
<br>
* [Surfline Dashboard](surfline-dashboard/README.md) - ★★☆☆☆
  * Very simple example of ETL pipeline which extracts data from Surfline API and loads it into PostgreSQL database using python code in Airflow
  * More complex than Reddit ETL Pipeline but still very simple
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
* [Audiophile End-To-End ELT Pipeline](audiophile-end-to-end-elt-pipeline/README.md) - ★★★★☆
  * Pipeline scrapes data from Crinacle's website and stores them as CSV files in S3 bucket
  * Data are then loaded into Redshift and PostgreSQL databases
  * dbt is used for data transformation
  * The whole pipeline is orchestrated by Airflow
  * Highlights:
    * Repository has very mature Makefile which allows to easily build and run the pipeline
    * GitHub Actions are used for CI/CD
    * AWS resoureces are managed by Terraform
  *