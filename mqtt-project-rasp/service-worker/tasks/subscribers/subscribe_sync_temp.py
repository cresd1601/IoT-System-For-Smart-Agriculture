from celery import signals
from sqlalchemy.orm import Session
from config import app
import json

from .helpers import mqtt_subscribe
from ..config.database import get_db


# Define a task to handle the subscription and processing of temperature sync messages
@app.task(bind=True)
def subscribe_sync_temp(self):
    mqtt_subscribe("group4/sync/temp", handle_message)

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def start_subscription_on_worker_ready(sender, **kwargs):
    subscribe_sync_temp.delay()

# Function to handle incoming MQTT messages and insert the data into the database
def handle_message(client, userdata, msg):
    # Parse the message payload
    sensor_id, temperature, humidity = parse_payload(msg.payload.decode('utf-8'))

    if sensor_id is not None and temperature is not None and humidity is not None:
        # Insert the record into the database
        save_temperature_record(sensor_id, temperature, humidity)
    else:
        print("Failed to process the message due to parsing error.")

# Function to parse the payload from the MQTT message
def parse_payload(payload):
    """
    Parses the payload from the MQTT message, expecting a JSON formatted string.
    """
    try:
        # Assuming the payload is a JSON string
        data = json.loads(payload)

        sensor_id = int(data.get('sensor_id'))
        temperature = float(data.get('temperature'))
        humidity = float(data.get('humidity'))

        return sensor_id, temperature, humidity
    except (KeyError, ValueError, json.JSONDecodeError) as e:
        print(f"Failed to parse payload: {e}")
        return None, None, None

# Function to save the temperature record into the database
def save_temperature_record(sensor_id, temperature, humidity):
    db: Session = next(get_db())

    try:
        sql = """
        INSERT INTO sensor_temperature_data (sensor_id, temperature, humidity)
        VALUES (:sensor_id, :temperature, :humidity)
        """
        db.execute(sql, {"sensor_id": sensor_id, "temperature": temperature, "humidity": humidity})
        db.commit()
    except Exception as e:
        db.rollback()  # Rollback in case of error
        print(f"Failed to insert record: {e}")
    finally:
        db.close()
