from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("SupplyChainStreamingPlatform") \
    .getOrCreate()

schema = StructType() \
    .add("shipment_id", StringType()) \
    .add("origin", StringType()) \
    .add("destination", StringType()) \
    .add("distance_km", IntegerType()) \
    .add("weight_tons", IntegerType()) \
    .add("event_timestamp", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","freight_events") \
    .load()

parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"),schema).alias("data")) \
    .select("data.*")

query = parsed.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()

