from datetime import datetime, timedelta
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..repositories.setting_repository import SettingRepository

class HumidityDataService:
    def __init__(self,
                 sensor_temperature_data_repository: SensorTemperatureDataRepository,
                 sensor_repository: SensorRepository,
                 location_repository: LocationRepository,
                 setting_repository: SettingRepository):
        self.repository = sensor_temperature_data_repository
        self.sensor_repository = sensor_repository
        self.location_repository = location_repository
        self.setting_repository = setting_repository

    def get_all_by_sensor_id(self, sensor_id):
        """Fetch detailed humidity data for the specific sensor_id."""
        humidity_data = self.repository.get_by_sensor_id(sensor_id)
        detailed_data = []

        if not humidity_data:
            return detailed_data

        sensor = self.sensor_repository.get_by_id(sensor_id)
        location = self.location_repository.get_by_id(sensor.location_id) if sensor else None

        for data in humidity_data:
            detailed_data.append({
                'id': data.id,
                'date_time': data.created_at,
                'sensor_name': sensor.name if sensor else 'Unknown Sensor',
                'location': location.name if location else 'Unknown Location',
                'humidity': data.humidity
            })

        return detailed_data

    def get_chart_data_by_sensor_id(self, sensor_id):
        """Fetch the latest 10 humidity records from the last 10 minutes for chart data,
        and include min and max humidity levels."""

        current_time = datetime.utcnow()
        start_time = current_time - timedelta(minutes=10)

        # Step 1: Fetch the latest 10 humidity records for the sensor within the time window
        humidity_records = self.repository.get_latest_by_sensor_id(sensor_id, start_time, limit=10)

        # Step 2: Fetch min and max humidity settings for the sensor
        settings = self.setting_repository.get_by_sensor_id(sensor_id)
        min_humidity = settings.min_humidity if settings else 0  # Default to 0 if no setting available
        max_humidity = settings.max_humidity if settings else 100  # Default to 100 if no setting available

        # Step 3: Format actual humidity data for chart display
        actual_humidity_data = [
            {"x": record.created_at.strftime("%H:%M"), "y": record.humidity}
            for record in humidity_records
        ]
        actual_humidity_data.reverse()

        # Step 4: Generate chart data for min and max values (static over the time range)
        min_humidity_data = [
            {"x": (current_time - timedelta(minutes=i)).strftime("%H:%M"), "y": min_humidity}
            for i in range(10)
        ]
        min_humidity_data.reverse()

        max_humidity_data = [
            {"x": (current_time - timedelta(minutes=i)).strftime("%H:%M"), "y": max_humidity}
            for i in range(10)
        ]
        max_humidity_data.reverse()

        # Step 5: Build the full chart data combining min, actual, and max humidity values
        chart_data = [
            {"id": "Minimum", "color": "blue", "data": min_humidity_data},
            {"id": "Humidity", "color": "green", "data": actual_humidity_data},
            {"id": "Maximum", "color": "red", "data": max_humidity_data}
        ]

        return chart_data
