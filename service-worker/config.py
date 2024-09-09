import os
from celery import Celery

# MQTT Setup
MQTT_BROKER = os.getenv('SERVICE_IP')
MQTT_PORT = 1883

print(f"MQTT Broker is set to: {MQTT_BROKER}")

# Initialize Celery
app = Celery(
    'service_worker', 
    broker = os.getenv('REDIS_URL'), 
    backend = os.getenv('REDIS_URL'), 
    broker_connection_retry_on_startup=True
)

# Manually import tasks
import tasks.publishers.publish_trigger_fan
import tasks.publishers.publish_trigger_pump
import tasks.subscribers.subscribe_sync_temp
import tasks.subscribers.subscribe_sync_moist
import tasks.subscribers.subscribe_track_device
import tasks.subscribers.subscribe_track_temp
import tasks.subscribers.subscribe_track_moist

