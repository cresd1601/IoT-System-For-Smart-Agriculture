from config import app
from .helpers import mqtt_publish

PUBLISH_TOPIC = 'group4/trigger/lcd'

@app.task(bind=True, name='service_worker.publish_trigger_lcd')
def publish_trigger_lcd(self, payload):
    mqtt_publish(PUBLISH_TOPIC, payload, retain=True)
