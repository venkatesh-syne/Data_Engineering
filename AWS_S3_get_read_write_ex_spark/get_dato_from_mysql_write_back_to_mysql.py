from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("MySQL Read Write Example") \
    .config(
        "spark.jars",
        "file:///C:/mysql/mysql-connector-j-8.0.33.jar"
    ) \
    .getOrCreate()

# MySQL connection details
url = "jdbc:mysql://localhost:3306/hospital"

properties = {
    "user": "root",
    "password": "root123",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# =========================
# READ DATA FROM MYSQL
# =========================
df = spark.read.jdbc(
    url=url,
    table="bills",
    properties=properties
)

print("Data from MySQL")
df.show()

# =========================
# TRANSFORM DATA
# =========================
from pyspark.sql.functions import col

df_updated = df.withColumn(
    "amount_increment",
    col("amount") + 1000
)

print("Transformed Data")
df_updated.show()

# =========================
# WRITE DATA TO MYSQL
# =========================
df_updated.write.jdbc(
    url=url,
    table="bills_updated",
    mode="overwrite",   # append / overwrite
    properties=properties
)

print("Data loaded successfully into MySQL")