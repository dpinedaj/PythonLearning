
import sys
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("azure-eventhub==1.3.1")
install("azure-eventhub-checkpointstoreblob-aio")
install("nest_asyncio")

import asyncio
import nest_asyncio
nest_asyncio.apply()
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

CONN_STR = 'Endpoint=sb://poccompensar.servicebus.windows.net/;SharedAccessKeyName=AppEventHubAccess;SharedAccessKey=m3bOLh2VwKgw1gWc0eCdFiCqRRY8HOqiUA6K57vtFjc='

def define_data():
    from pyspark import SparkContext
    from pyspark.sql import SparkSession
    install("pandas")
    import pandas as pd
    sc = SparkContext("local[*]", "test").getOrCreate()
    spark = SparkSession.builder.master("local[*]").getOrCreate()

    batch_size = 100
    data = [[i, i*35] for i in range(batch_size*10000)]
    dataFrame = sc.parallelize(data).toDF(["test", "test2"])
    df = dataFrame.toPandas()
    return df, batch_size


async def run(data, batch_size):

    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONN_STR, eventhub_name="pruebacompensar")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()


        for _ in range(0, len(data), batch_size):
            actual_state = 0

            for index in range(actual_state, actual_state + batch_size):
        
                # Add events to the batch
                event_data_batch.add(EventData(str(data.iloc[index])))

            # Send the batch of events to the event hub.
            print(f"sending batch of size: {batch_size}")
            await producer.send_batch(event_data_batch)
            actual_state += batch_size
if __name__ == "__main__":
    data, batch_size = define_data()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(data, batch_size))
