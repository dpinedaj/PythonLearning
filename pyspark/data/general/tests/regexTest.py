from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import functions as f

sc = SparkContext("local[*]", "test").getOrCreate()
spark = SparkSession.builder.master("local[*]").getOrCreate()


regExp = r"^[\w - \.]+@([\w -]+\.)+[\w -]{2,4}$"


columns = ["correo"]

data = [["dpinedaj@unal.edu.co"],
        ["vanesalo10@gmail.com"],
        ["dpineda@other.com"],
        ["jass.com"],
        ["TestMail"]]

df = sc.parallelize(data).toDF(columns)

df2 = df.withColumn("validation", f.when(f.regexp_extract(
    "correo", regExp, 1) != '', f.lit(True)).otherwise(f.lit(False)))
