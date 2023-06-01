# Data platform - case studies
* In this repository I document my research of different existing DP / ETL solutions which are publicly available on GitHub
* I heavily utilized AI tools for this project - ChatGPT-4, ChatSonic and Github Copilot

## Table of contents
I will rate each project by stars (★☆☆☆☆ / ★★☆☆☆ / ★★★☆☆ / ★★★★☆ / ★★★★★) based on my opinion about the project after analyzing its code and documentation.

* [Reddit ETL Pipeline](reddit-etl-pipeline/README.md) - ★☆☆☆☆
  * This is a very simple example of ETL pipeline which extracts data from Reddit API and loads it into AWS Redshift using python code in Airflow
  * AWS parts are terraformed.
* [Finnhub Streaming Data Pipeline](finnhub-streaming-data-pipeline/README.md) - ★★★☆☆
  * This is a very interesting implementation of streaming data pipeline which uses Finnhub.io API/websocket to get real-time trading data
  * Data are scraped from websocket using python code and ingested into Kafka broker
  * Kafka is managed by Zookeeper and Kafdrop
  * Scala application running on Spark Kubernetes cluster is consuming data from Kafka and loads them into Cassandra tables
    * Repository contains Dockerfile showing how to build Cassandra image with setup `.cql` script, which creates Cassandra tables on startup
  * Grafana is used for visualization
    * Repository contains Dockerfile demonstrating how to build Grafana image with Cassandra plugin and predefined dashboards
  * All parts are containerized into Docker containers and orchestrated by Kubernetes, deploymend and infrastructure is managed by Terraform
*