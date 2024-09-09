from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository

class HumidityDataService:
    def __init__(self,
                 sensor_temperature_data_repository: SensorTemperatureDataRepository,
                 sensor_repository: SensorRepository,
                 location_repository: LocationRepository):
        self.repository = sensor_temperature_data_repository
        self.sensor_repository = sensor_repository
        self.location_repository = location_repository

    def get_all_by_sensor_id(self, sensor_id):
        # Fetch all temperature data for the specific sensor_id
        temperature_data = self.repository.get_by_sensor_id(sensor_id)
        detailed_data = []

        if not temperature_data:
            return detailed_data  # Return empty list if no data

        # Fetch the sensor
        sensor = self.sensor_repository.get_by_id(sensor_id)

        # Fetch the location associated with the sensor
        location = self.location_repository.get_by_id(sensor.location_id) if sensor else None

        # Construct detailed data
        for data in temperature_data:
            detailed_data.append({
                'id': data.id,
                'date_time': data.created_at,
                'sensor_name': sensor.name if sensor else 'Unknown Sensor',
                'location': location.name if location else 'Unknown Location',
                'humidity': data.humidity
            })

        return detailed_data
