from ..models.sensor_model import SensorModel  # Import the SensorModel
from ..repositories.sensor_repository import SensorRepository  # Import the SensorRepository

class SensorService:
    def __init__(self, sensor_repository: SensorRepository):
        self.sensor_repository = sensor_repository

    # Get all sensors with data parsing
    def get_all(self):
        sensors = self.sensor_repository.get_all()

        return [
            {
                'id': sensor.id,
                'name': sensor.name,
                'type_id': sensor.type_id,
                'location_id': sensor.location_id,
                'type': sensor.type.type if sensor.type else None,
                'location': sensor.location.name if sensor.location else None
            } for sensor in sensors
        ]

    # Create a new sensor
    def create(self, sensor_data):
        new_sensor = SensorModel(
            name=sensor_data.get("name"),
            type_id=sensor_data.get("type_id"),
            location_id=sensor_data.get("location_id")
        )

        created_sensor = self.sensor_repository.create(new_sensor)

        if created_sensor:
            return {
                'id': created_sensor.id,
                'name': created_sensor.name,
                'type_id': created_sensor.type_id,
                'location_id': created_sensor.location_id,
                'type': created_sensor.type.type if created_sensor.type else None,
                'location': created_sensor.location.name if created_sensor.location else None
            }

        return None

    # Get a sensor by ID
    def get_by_id(self, sensor_id):
        sensor = self.sensor_repository.get_by_id(sensor_id)

        if sensor:
            return {
                'id': sensor.id,
                'name': sensor.name,
                'type_id': sensor.type_id,
                'location_id': sensor.location_id,
                'type': sensor.type.type if sensor.type else None,
                'location': sensor.location.name if sensor.location else None
            }

        return None

    # Update a sensor by ID
    def update(self, sensor_id, sensor_data):
        sensor = self.sensor_repository.get_by_id(sensor_id)

        if sensor:
            sensor.name = sensor_data.get("name")
            sensor.type_id = sensor_data.get("type_id")
            sensor.location_id = sensor_data.get("location_id")
            updated_sensor = self.sensor_repository.update(sensor)

            return {
                'id': updated_sensor.id,
                'name': updated_sensor.name,
                'type_id': updated_sensor.type_id,
                'location_id': updated_sensor.location_id,
                'type': updated_sensor.type.type if updated_sensor.type else None,
                'location': updated_sensor.location.name if updated_sensor.location else None
            }
        return None

    # Delete a sensor by ID
    def delete(self, sensor_id):
        return self.sensor_repository.delete(sensor_id)
