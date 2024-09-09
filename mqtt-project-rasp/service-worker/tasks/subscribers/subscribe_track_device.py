from celery import signals
from config import app
from .helpers import mqtt_subscribe
from ..publishers.publish_trigger_lcd import publish_trigger_lcd  # Import for LCD publish

# States to keep track of
class DeviceState:
    def __init__(self):
        self.fan_state = "OFF"
        self.pump_state = "OFF"
        self.last_lcd_message = ""

    def update_state(self, pump_state=None, fan_state=None):
        if pump_state:
            self.pump_state = pump_state
        if fan_state:
            self.fan_state = fan_state

    def determine_lcd_message(self):
        if self.pump_state == "ON" or self.fan_state == "ON":
            return "IoT System Running..."
        return "Perfect Environment"

device_state = DeviceState()  # Initialize the device state

# MQTT topics
topic_pump = "group4/trigger/pump"
topic_fan = "group4/trigger/fan"

# Function to handle incoming MQTT messages
def handle_mqtt_message(client, userdata, msg):
    global device_state

    # Decode the RAW payload to a string
    message = msg.payload.decode('utf-8').strip()
    print(f"Message received: {msg.topic} -> {message}")

    # Update the state based on the received message
    if msg.topic == topic_pump:
        device_state.update_state(pump_state=message)
    elif msg.topic == topic_fan:
        device_state.update_state(fan_state=message)

    # Determine the message to publish to the LCD topic
    new_message = device_state.determine_lcd_message()

    # Publish only if the message has changed
    if new_message != device_state.last_lcd_message:
        publish_trigger_lcd.delay(new_message)  # Use the LCD publisher task
        print(f"Published to LCD: {new_message}")
        device_state.last_lcd_message = new_message

# Celery task to subscribe to the topics
@app.task(bind=True)
def subscribe_sync_device(self):
    mqtt_subscribe([(topic_pump, 0), (topic_fan, 0)], handle_mqtt_message)
    print(f"Subscribed to topics: {topic_pump}, {topic_fan}")

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def when_worker_ready(sender, **kwargs):
    subscribe_sync_device.delay()
