from config import app
from .helpers import mqtt_publish

PUBLISH_TOPIC = 'group4/trigger/fan'

@app.task(bind=True, name='service_worker.publish_trigger_fan')
def publish_trigger_fan(self, fan_state):
    """
    Publish the fan state to the MQTT topic.

    Args:
        fan_state (str): The state of the fan, either 'ON' or 'OFF'.
    """
    mqtt_publish(PUBLISH_TOPIC, fan_state, retain=True)
