import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT

def mqtt_publish(topic, payload, retain=False):
    """
    Publish a message to the MQTT topic.

    Args:
        topic (str): The MQTT topic to publish to.
        payload (str): The message payload.
        retain (bool): Whether to retain the message on the broker.
    """
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result code {rc}")

    def on_publish(client, userdata, mid):
        print(f"Message published successfully with mid: {mid}")

    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connect to the MQTT broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Start the loop in a non-blocking way
    client.loop_start()

    # Publish the message with the retain flag
    result = client.publish(topic, payload, retain=retain)

    # Add a check to see if the publish was successful
    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"Publishing message '{payload}' to topic '{topic}' with retain={retain}")
    else:
        print(f"Failed to publish message '{payload}' with error code: {result.rc}")

    # Stop the loop after publishing
    client.loop_stop()
