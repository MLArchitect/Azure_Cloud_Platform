# Databricks notebook source

# COMMAND ----------

# Configure OAuth connection to Azure Data Lake Storage
spark.conf.set("fs.azure.account.auth.type.databricksen.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.databricksen.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.databricksen.dfs.core.windows.net", "<YOUR-CLIENT-ID>")
spark.conf.set("fs.azure.account.oauth2.client.secret.databricksen.dfs.core.windows.net", "<YOUR-CLIENT-SECRET>")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.databricksen.dfs.core.windows.net", "https://login.microsoftonline.com/<YOUR-TENANT-ID>/oauth2/token")

# COMMAND ----------

# List files in the source container to verify connection
dbutils.fs.ls("abfss://source@databricksen.dfs.core.windows.net/")

# COMMAND ----------

# Read all 5 CSV files from the bronze layer into DataFrames
athletes = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@databricksen.dfs.core.windows.net/Athletes.csv")
coaches = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@databricksen.dfs.core.windows.net/Coaches.csv")
entriesgender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@databricksen.dfs.core.windows.net/EntriesGender.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@databricksen.dfs.core.windows.net/Medals.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("abfss://source@databricksen.dfs.core.windows.net/Teams.csv")

# COMMAND ----------

# Preview athletes data
athletes.show()

# COMMAND ----------

# Cast string columns to integer for numeric operations
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

entriesgender = entriesgender.withColumn("Female", col("Female").cast(IntegerType())) \
    .withColumn("Male", col("Male").cast(IntegerType())) \
    .withColumn("Total", col("Total").cast(IntegerType()))

medals = medals.withColumn("Rank", col("Rank").cast(IntegerType())) \
    .withColumn("Gold", col("Gold").cast(IntegerType())) \
    .withColumn("Silver", col("Silver").cast(IntegerType())) \
    .withColumn("Bronze", col("Bronze").cast(IntegerType())) \
    .withColumn("Total", col("Total").cast(IntegerType())) \
    .withColumn("Rank by Total", col("Rank by Total").cast(IntegerType()))

# COMMAND ----------

# Top countries by gold medals
medals.orderBy("Gold", ascending=False).select("Team_Country", "Gold").show()

# COMMAND ----------

# Gender ratio per discipline
from pyspark.sql.functions import format_number

average_entries_by_gender = entriesgender.withColumn(
    'Avg_Female', format_number(entriesgender['Female'] / entriesgender['Total'], 2)
).withColumn(
    'Avg_Male', format_number(entriesgender['Male'] / entriesgender['Total'], 2)
)
average_entries_by_gender.show()

# COMMAND ----------

# Write transformed data to silver layer
athletes.write.mode("overwrite").option("header","true").csv("abfss://source@databricksen.dfs.core.windows.net/silverath/athletes")
coaches.write.mode("overwrite").option("header","true").csv("abfss://source@databricksen.dfs.core.windows.net/silverath/coaches")
entriesgender.write.mode("overwrite").option("header","true").csv("abfss://source@databricksen.dfs.core.windows.net/silverath/entriesgender")
medals.write.mode("overwrite").option("header","true").csv("abfss://source@databricksen.dfs.core.windows.net/silverath/medals")
teams.write.mode("overwrite").option("header","true").csv("abfss://source@databricksen.dfs.core.windows.net/silverath/teams")
