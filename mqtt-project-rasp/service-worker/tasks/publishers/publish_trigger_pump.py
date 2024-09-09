from config import app
from .helpers import mqtt_publish

PUBLISH_TOPIC = 'group4/trigger/pump'

@app.task(bind=True, name='service_worker.publish_trigger_pump')
def publish_trigger_pump(self, payload):
    mqtt_publish(PUBLISH_TOPIC, payload, retain=True)
