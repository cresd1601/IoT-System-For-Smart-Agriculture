from celery import signals
from config import app
from .helpers import mqtt_subscribe
from ..publishers.publish_trigger_pump import publish_trigger_pump
from ..config.database import get_db
import json
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize the pump state (assuming the pump is initially OFF)
pump_state = "OFF"

def fetch_moisture_thresholds(db, sensor_id):
    """
    Fetch the max and min moisture for a given sensor_id from the database.
    """
    sql = """
        SELECT max_moisture, min_moisture
        FROM settings
        WHERE sensor_id = :sensor_id
    """
    try:
        result = db.execute(sql, {"sensor_id": sensor_id}).fetchone()
        if result:
            logger.debug(f"Fetched thresholds for sensor_id {sensor_id}: {result}")
        else:
            logger.warning(f"No moisture thresholds found for sensor_id {sensor_id}")
        return result
    except Exception as e:
        logger.error(f"Error fetching moisture thresholds for sensor_id {sensor_id}: {e}", exc_info=True)
        return None

def determine_pump_action(soil_moisture, min_moisture):
    """
    Determine whether to turn the pump ON or OFF based on soil moisture.
    """
    action = "ON" if soil_moisture < min_moisture else "OFF"
    logger.debug(f"Pump action based on soil_moisture {soil_moisture} and min_moisture {min_moisture}: {action}")
    return action

def handle_mqtt_message(client, userdata, msg):
    """
    Handle the incoming MQTT message, determine pump action based on the
    sensor's moisture thresholds, and trigger the pump if needed.
    """
    global pump_state

    try:
        # Parse the incoming JSON payload
        data = json.loads(msg.payload.decode('utf-8'))
        logger.debug(f"Received MQTT message: {data}")

        soil_moisture = data.get('soil_moisture')
        sensor_id = data.get('sensor_id')

        if soil_moisture is None or sensor_id is None:
            logger.warning(f"Invalid message payload: {msg.payload}")
            return

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
                logger.info(f"Pump state updated to: {pump_state}")

    except (KeyError, ValueError) as e:
        logger.error(f"Error processing MQTT message: {e}", exc_info=True)
    finally:
        # Ensure the database connection is closed
        if 'db' in locals():
            db.close()

# Define the Celery task for subscribing to the MQTT topic
@app.task(bind=True)
def subscribe_track_moist(self):
    """
    Subscribe to the MQTT topic for moisture tracking.
    """
    logger.info("Subscribing to MQTT topic group4/track/moist")
    mqtt_subscribe("group4/track/moist", handle_mqtt_message)

# Signal handler to start the subscription after the worker is fully configured
@signals.worker_ready.connect
def start_subscription_on_worker_ready(sender, **kwargs):
    """
    Start MQTT subscription when the Celery worker is ready.
    """
    logger.info("Starting MQTT subscription after Celery worker is ready")
    subscribe_track_moist.delay()
