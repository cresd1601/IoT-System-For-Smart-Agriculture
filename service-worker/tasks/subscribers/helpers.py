import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT

def mqtt_subscribe(topic, on_message_callback):
    def on_connect(client, userdata, flags, rc):
        client.subscribe(topic)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message_callback

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()