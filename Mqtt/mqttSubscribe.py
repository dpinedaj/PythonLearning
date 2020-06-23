import paho.mqtt.client as mqtt
import json


broker="tailor.cloudmqtt.com"
port=14908
username=""
password=""

mensajes = []

def on_message(client, obj, msg):
    global mensajes
    
    mensaje = json.loads(msg.payload.decode('utf-8'))
    print(f'Received {msg.topic} (QoS: {msg.qos}): {mensaje}')
    mensajes.append(mensaje)

if __name__ == '__main__':
    try:
        while True:
            client = mqtt.Client()
            client.username_pw_set(username, password)

            client.on_message = on_message

            client.connect(broker, port)
            client.subscribe('pi')

            print('Listening...')

            client.loop_forever()
    except KeyboardInterrupt:
        print('Closing')
        client.disconnect()
        exit()


