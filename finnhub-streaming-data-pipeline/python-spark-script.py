## this file contains mockup of python script for Spark job which reads data from Kafka and writes them into Cassandra

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, current_timestamp, udf
from pyspark.sql.avro.functions import from_avro
from pyspark.sql.streaming import Trigger
from pyspark.sql.types import StringType
import uuid

# UDF for generating UUIDs
def make_uuid():
    return str(uuid.uuid1())

uuid_udf = udf(make_uuid, StringType())

# Create Spark session
spark = SparkSession.builder \
    .appName("StreamProcessor") \
    .getOrCreate()

# Read streams from Kafka
input_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "<kafka_server_address>") \
    .option("subscribe", "<kafka_topic>") \
    .load()

# Explode the data from Avro
expanded_df = input_df \
    .select(from_avro(col("value"), "<avro_schema>").alias("avroData")) \
    .select("avroData.*") \
    .select(explode(col("data")).alias("col"))

# Rename columns and add proper timestamps
final_df = expanded_df \
    .withColumn("uuid", uuid_udf()) \
    .withColumnRenamed("c", "trade_conditions") \
    .withColumnRenamed("p", "price") \
    .withColumnRenamed("s", "symbol") \
    .withColumnRenamed("t", "trade_timestamp") \
    .withColumnRenamed("v", "volume") \
    .withColumn("trade_timestamp", (col("trade_timestamp") / 1000).cast("timestamp")) \
    .withColumn("ingest_timestamp", current_timestamp())

# Write query to Cassandra
query = final_df \
    .writeStream \
    .outputMode("update") \
    .foreachBatch(lambda df, epoch_id: df.write \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="<cassandra_table>", keyspace="<cassandra_keyspace>") \
        .mode("append") \
        .save()) \
    .start()

# Another dataframe with aggregates - running averages from last 15 seconds
summary_df = final_df \
    .withColumn("price_volume_multiply", col("price") * col("volume")) \
    .withWatermark("trade_timestamp", "15 seconds") \
    .groupBy("symbol") \
    .avg("price_volume_multiply")

# Rename columns in dataframe and add UUIDs before inserting to Cassandra
final_summary_df = summary_df \
    .withColumn("uuid", uuid_udf()) \
    .withColumn("ingest_timestamp", current_timestamp()) \
    .withColumnRenamed("avg(price_volume_multiply)", "price_volume_multiply")

# Write second query to Cassandra
query2 = final_summary_df \
    .writeStream \
    .trigger(Trigger.ProcessingTime("5 seconds")) \
    .outputMode("update") \
    .foreachBatch(lambda df, epoch_id: df.write \
        .format("org.apache.spark.sql.cassandra") \
        .options(table="<cassandra_table>", keyspace="<cassandra_keyspace>") \
        .mode("append") \
        .save()) \
    .start()

# Let query await termination
spark.streams.awaitAnyTermination()
