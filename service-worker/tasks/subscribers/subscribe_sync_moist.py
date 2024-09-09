from celery import signals
from sqlalchemy.orm import Session
from config import app
import json

from .helpers import mqtt_subscribe
from ..config.database import get_db


# Define a task to handle the subscription and processing of moisture sync messages
@app.task(bind=True)
def subscribe_sync_moist(self):
    mqtt_subscribe("group4/sync/moist", handle_moisture_message)

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def start_subscription_on_worker_ready(sender, **kwargs):
    subscribe_sync_moist.delay()

# Function to handle incoming MQTT messages and insert the data into the database
def handle_moisture_message(client, userdata, msg):
    # Parse the message payload
    sensor_id, moisture = parse_moisture_payload(msg.payload.decode('utf-8'))

    if sensor_id is not None and moisture is not None:
        # Insert the record into the database
        save_moisture_record(sensor_id, moisture)
    else:
        print("Failed to process the message due to parsing error.")

# Function to parse the payload from the MQTT message
def parse_moisture_payload(payload):
    """
    Parses the payload from the MQTT message, expecting a JSON formatted string.
    """
    try:
        # Assuming the payload is a JSON string
        data = json.loads(payload)

        sensor_id = int(data.get('sensor_id'))
        moisture = float(data.get('soil_moisture'))

        return sensor_id, moisture
    except (KeyError, ValueError, json.JSONDecodeError) as e:
        print(f"Failed to parse payload: {e}")
        return None, None

# Function to save the moisture record into the database
def save_moisture_record(sensor_id, moisture):
    db: Session = next(get_db())

    try:
        sql = """
        INSERT INTO sensor_moisture_data (sensor_id, moisture)
        VALUES (:sensor_id, :moisture)
        """
        db.execute(sql, {"sensor_id": sensor_id, "moisture": moisture})
        db.commit()
    except Exception as e:
        db.rollback()  # Rollback in case of error
        print(f"Failed to insert record: {e}")
    finally:
        db.close()
