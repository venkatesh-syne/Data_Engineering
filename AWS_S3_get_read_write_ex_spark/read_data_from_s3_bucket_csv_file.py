from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("S3 Read") \
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.3.4"
    ) \
    .getOrCreate()

hadoop_conf = spark._jsc.hadoopConfiguration()

hadoop_conf.set(
    "fs.s3a.aws.credentials.provider",
    "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
)


df = spark.read \
    .option("header", "true") \
    .csv("s3a://venky-de-bucket/student_performance.csv")


df.show()