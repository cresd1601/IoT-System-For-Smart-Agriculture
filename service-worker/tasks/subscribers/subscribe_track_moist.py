from celery import signals
from config import app
from .helpers import mqtt_subscribe
from ..publishers.publish_trigger_pump import publish_trigger_pump
from ..config.database import get_db
import json

# Initialize the pump state (assuming the pump is initially OFF)
pump_state = "OFF"

def fetch_moisture_thresholds(db, sensor_id):
    """Fetch the max and min moisture for a given sensor_id from the database."""
    sql = """
        SELECT max_moisture, min_moisture
        FROM settings
        WHERE sensor_id = :sensor_id
    """
    return db.execute(sql, {"sensor_id": sensor_id}).fetchone()

# DEVELOPING, NEED FUNDING FROM YOU, SHARKKKKK !!!
def determine_dryer_action(temperature, max_moisture):
    """Determine whether to turn the heater ON or OFF based on temperature."""
    return "ON" if temperature > max_moisture else "OFF"

def determine_pump_action(soil_moisture, min_moisture):
    """Determine whether to turn the pump ON or OFF based on soil moisture."""
    return "ON" if soil_moisture < min_moisture else "OFF"

def handle_mqtt_message(client, userdata, msg):
    global pump_state

    # Parse the incoming JSON payload
    data = json.loads(msg.payload.decode('utf-8'))
    soil_moisture = data.get('soil_moisture')
    sensor_id = data.get('sensor_id')

    if soil_moisture is None or sensor_id is None:
        return

    try:
        # Get the database session
        db = next(get_db())

        # Fetch the moisture thresholds for the given sensor_id
        result = fetch_moisture_thresholds(db, sensor_id)

        if result:
            max_moisture, min_moisture = result

            # Determine the pump action based on the current soil moisture
            action = determine_pump_action(soil_moisture, min_moisture)

            # Avoid sending duplicate requests by checking the current pump state
            if action and action != pump_state:
                publish_trigger_pump(action)
                pump_state = action  # Update the pump state

    except Exception as e:
        pass
    finally:
        db.close()

# Define the Celery task for subscribing to the MQTT topic
@app.task(bind=True)
def subscribe_track_moist(self):
    mqtt_subscribe("group4/track/moist", handle_mqtt_message)

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def start_subscription_on_worker_ready(sender, **kwargs):
    subscribe_track_moist.delay()
