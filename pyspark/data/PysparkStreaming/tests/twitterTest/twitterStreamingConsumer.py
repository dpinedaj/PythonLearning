#Install packages
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pandas")
install("matplotlib")
install("seaborn")


#pyspark needed packages
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import desc


# Other libraries
from collections import namedtuple
import time
from IPython import display
import matplotlib.pyplot as plt
import seaborn as sns
import pandas

sc = SparkContext("local[*]", "twitterExample")

ssc = StreamingContext(sc, 10)
sqlContext = SQLContext(sc)

socket_stream = ssc.socketTextStream("127.0.0.1", 5555)
lines = socket_stream.window(20)
fields = ("tag", "count")
Tweet = namedtuple('Tweet', fields)

data = (lines.flatMap(lambda text: text.split(" "))  # Splits to a list
        # Checks for hashtag calls
        .filter(lambda word: word.lower().startswith("#"))
        .map(lambda word: (word.lower(), 1))  # Lower cases the word
        .reduceByKey(lambda a, b: a + b)  # Reduces
        .map(lambda rec: Tweet(rec[0], rec[1]))  # Stores in a Tweet Object
        .foreachRDD(lambda rdd: rdd.toDF().sort(desc("count"))  # Sorts Them in a DF
                    .limit(10).registerTempTable("tweets")))  # Registers to a table.


ssc.start()

count = 0
while count < 1000:
    
    time.sleep( 3 )
    top_10_tweets = sqlContext.sql( 'Select tag, count from tweets' )
    top_10_df = top_10_tweets.toPandas()
    display.clear_output(wait=True)
    plt.figure( figsize = ( 10, 8 ) )
    sns.barplot( x="count", y="tag", data=top_10_df)
    plt.show()
    count = count + 1


ssc.stop()