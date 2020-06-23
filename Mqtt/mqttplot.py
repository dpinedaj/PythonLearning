import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plt


topic = ""
username  = ""
password    = ""
broker="tailor.cloudmqtt.com"
port=14908


#import DataPlot and RealtimePlot from the file plotData.py
from plotData import DataPlot, RealtimePlot

fig, axes = plt.subplots()
plt.title('Data from TTN console')

data = DataPlot()
dataPlotting= RealtimePlot(axes)

count=0


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

def on_message(client, userdata, msg):
    j_msg = json.loads(msg.payload.decode('utf-8'))
    number= j_msg

    

    # plot data
    global count
    count+=1
    data.add(count,number)
    dataPlotting.plot(data)
    plt.pause(0.001)


# set paho.mqtt callback
ttn_client = mqtt.Client()
ttn_client.on_connect = on_connect
ttn_client.on_message = on_message
ttn_client.username_pw_set(username, password)
ttn_client.connect(broker,port,60) #MQTT port over TLS

try:
    ttn_client.loop_forever()
except KeyboardInterrupt:
    print('disconnect')
    ttn_client.disconnect()