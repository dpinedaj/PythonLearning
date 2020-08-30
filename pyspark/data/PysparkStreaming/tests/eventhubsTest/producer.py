import sys
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("azure-eventhub==1.3.1")
from pyspark.sql import functions as f
from pyspark import SparkContext
from pyspark.sql import SparkSession
import time
import logging
from azure.eventhub import EventHubClient, EventData






logger = logging.getLogger("azure")

sc = SparkContext("local[*]", "test").getOrCreate()
spark = SparkSession.builder.master("local[*]").getOrCreate()

ADDRESS = "amqps://poccompensar.servicebus.windows.net/pruebacompensar"
USER = "AppEventHubAccess"
KEY = "m3bOLh2VwKgw1gWc0eCdFiCqRRY8HOqiUA6K57vtFjc="

try:
    if not ADDRESS:
        raise ValueError("No EventHubs URL supplied.")

    # Create Event Hubs client
    client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
    sender = client.add_sender(partition="0")
    client.run()
    try:
        start_time = time.time()
        data = [[i, i*35] for i in range(1000*1000)]
        dataFrame = sc.parallelize(data).toDF(["test", "test2"])
        size = dataFrame.count()
        for index in range(0, size, 100):
            print("Sending message: {}".format(
                str(dataFrame.filter(f.col("test").between(index, index + 100)))))
            sender.send(EventData(str(dataFrame.filter(f.col("test").between(index, index + 100)))))

    except:
        raise
    finally:
        end_time = time.time()
        client.stop()
        run_time = end_time - start_time
        logger.info("Runtime: {} seconds".format(run_time))

except KeyboardInterrupt:
    client.stop()
