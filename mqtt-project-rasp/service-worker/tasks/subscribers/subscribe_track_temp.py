from celery import signals
from config import app
from .helpers import mqtt_subscribe
from ..publishers.publish_trigger_fan import publish_trigger_fan
from ..config.database import get_db
import json

# Initialize the fan state (assuming the fan is initially OFF)
fan_state = "OFF"

def fetch_temperature_thresholds(db, sensor_id):
    """Fetch the max and min temperature for a given sensor_id from the database."""
    sql = """
        SELECT max_temperature, min_temperature
        FROM settings
        WHERE sensor_id = :sensor_id
    """
    return db.execute(sql, {"sensor_id": sensor_id}).fetchone()

# DEVELOPING, NEED FUNDING FROM YOU, SHARKKKKK !!!
def determine_heater_action(temperature, min_temp):
    """Determine whether to turn the heater ON or OFF based on temperature."""
    return "ON" if temperature < min_temp else "OFF"

def determine_fan_action(temperature, max_temp):
    """Determine whether to turn the fan ON or OFF based on temperature."""
    return "ON" if temperature > max_temp else "OFF"

def handle_mqtt_message(client, userdata, msg):
    global fan_state

    # Parse the incoming JSON payload
    data = json.loads(msg.payload.decode('utf-8'))
    temperature = data.get('temperature')
    sensor_id = data.get('sensor_id')

    if temperature is None or sensor_id is None:
        return

    try:
        # Get the database session
        db = next(get_db())

        # Fetch the temperature thresholds for the given sensor_id
        result = fetch_temperature_thresholds(db, sensor_id)

        if result:
            max_temp, min_temp = result

            # Determine the fan action based on the current temperature
            fan_action = determine_fan_action(temperature, max_temp)

        # Avoid sending duplicate requests by checking the current fan state
            if fan_action and fan_action != fan_state:
                publish_trigger_fan(fan_action)
                fan_state = fan_action  # Update the fan state

    except Exception as e:
        pass
    finally:
        db.close()

# Define the Celery task for subscribing to the MQTT topic
@app.task(bind=True)
def subscribe_sync_temp(self):
    mqtt_subscribe("group4/track/temp", handle_mqtt_message)

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def start_subscription_on_worker_ready(sender, **kwargs):
    subscribe_sync_temp.delay()
