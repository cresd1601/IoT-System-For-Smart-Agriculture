from celery import signals
from config import app
from .helpers import mqtt_subscribe
from ..publishers.publish_trigger_lcd import publish_trigger_lcd  # Import for LCD publish

# States to keep track of
fan_state = "OFF"
pump_state = "OFF"
last_lcd_message = ""

# MQTT topics
topic_pump = "group4/trigger/pump"
topic_fan = "group4/trigger/fan"

# Function to determine the message to publish based on pump and fan states
def determine_lcd_message(pump_state, fan_state):
    if pump_state == "ON" or fan_state == "ON":
        return "IoT System Running..."
    return "Perfect Environment"

# Function to handle incoming MQTT messages
def handle_mqtt_message(client, userdata, msg):
    global fan_state, pump_state, last_lcd_message

    # Decode the RAW payload to a string
    message = msg.payload.decode('utf-8').strip()
    print(f"Message received: {msg.topic} -> {message}")

    # Update the state based on the received message
    if msg.topic == topic_pump:
        pump_state = message
    elif msg.topic == topic_fan:
        fan_state = message

    # Determine the message to publish to the LCD topic
    new_message = determine_lcd_message(pump_state, fan_state)

    # Publish only if the message has changed
    if new_message != last_lcd_message:
        publish_trigger_lcd.delay(new_message)  # Use the LCD publisher task
        print(f"Published to LCD: {new_message}")
        last_lcd_message = new_message

# Celery task to subscribe to the topics
@app.task(bind=True)
def subscribe_sync_device(self):
    mqtt_subscribe([(topic_pump, 0), (topic_fan, 0)], handle_mqtt_message)
    print(f"Subscribed to topics: {topic_pump}, {topic_fan}")

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def when_worker_ready(sender, **kwargs):
    subscribe_sync_device.delay()
