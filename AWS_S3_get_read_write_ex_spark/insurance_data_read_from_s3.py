from pyspark.sql import SparkSession
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['HADOOP_HOME'] = r"C:\hadoop"
#os.environ['PATH'] += r"C:\hadoop\bin"
os.environ["HADOOP_OPTS"] = "-Djava.library.path=C:\\hadoop\\bin"
os.environ["PATH"] += r";C:\hadoop\bin"

spark = SparkSession.builder \
    .appName("Insurance-Medallion") \
    .master("local[*]") \
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.11.1026"
    ) \
    .config(
        "spark.cleaner.referenceTracking.cleanCheckpoints",
        "false"
    ) \
    .getOrCreate()

# AWS Credentials
hadoop_conf = spark._jsc.hadoopConfiguration()

hadoop_conf.set(
    "fs.s3a.aws.credentials.provider",
    "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
)


# Read files from S3
claims_raw = spark.read.option("header", True).csv(
    "s3a://venky-de-bucket/claims.csv"
)

customers_raw = spark.read.option("header", True).csv(
    "s3a://venky-de-bucket/customers.csv"
)

policies_raw = spark.read.option("header", True).csv(
    "s3a://venky-de-bucket/policies.csv"
)

payments_raw = spark.read.option("header", True).csv(
    "s3a://venky-de-bucket/payments.csv"
)

""" claims_raw.show()
customers_raw.show()
policies_raw.show()
payments_raw.show()  """

customers_raw.write.mode("overwrite").csv("data/bronze/customers")
policies_raw.write.mode("overwrite").csv("data/bronze/policies")
claims_raw.write.mode("overwrite").parquet("data/bronze/claims")
payments_raw.write.mode("overwrite").parquet("data/bronze/payments")

customers = spark.read.parquet("data/bronze/customers")
policies  = spark.read.parquet("data/bronze/policies")
claims    = spark.read.parquet("data/bronze/claims")
payments  = spark.read.parquet("data/bronze/payments")

