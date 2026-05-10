from pyspark.sql import SparkSession
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()

df = spark.createDataFrame([(1,"a"),(2,"b")],["id","name"])

df.write.mode("overwrite").csv("test_output") #test_output is a folder

print("SUCCESS")