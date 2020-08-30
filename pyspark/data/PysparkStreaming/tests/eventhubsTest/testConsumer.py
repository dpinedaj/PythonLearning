from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from azure import eventhub

sc = SparkContext("local[*]", "eventhubExample")
ssc = StreamingContext(sc, 10)
spark = SparkSession.builder.master("local[*]").getOrCreate()


# Source with default settings
CONN_STR = 'Endpoint=sb://poccompensar.servicebus.windows.net/;SharedAccessKeyName=AppEventHubAccess;SharedAccessKey=m3bOLh2VwKgw1gWc0eCdFiCqRRY8HOqiUA6K57vtFjc='

ehConf = {
  'eventhubs.connectionString' : CONN_STR
}


df = spark \
  .readStream \
  .format("eventhubs") \
  .options(**ehConf) \
  .load()