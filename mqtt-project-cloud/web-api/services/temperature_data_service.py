from datetime import datetime, timedelta
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..repositories.setting_repository import SettingRepository

class TemperatureDataService:
    def __init__(self,
                 temperature_data_repository: SensorTemperatureDataRepository,
                 sensor_repository: SensorRepository,
                 location_repository: LocationRepository,
                 setting_repository: SettingRepository):
        self.repository = temperature_data_repository
        self.sensor_repository = sensor_repository
        self.location_repository = location_repository
        self.setting_repository = setting_repository

    def get_all_by_sensor_id(self, sensor_id):
        """Fetch detailed temperature data for the specific sensor_id."""
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
                'temperature': data.temperature
            })

        return detailed_data

    def get_chart_data_by_sensor_id(self, sensor_id):
        """Fetch the latest 10 temperature records from the last 10 minutes for chart data,
        and include min and max temperature levels."""

        # Step 1: Calculate the time window for the last 10 minutes
        current_time = datetime.utcnow()
        start_time = current_time - timedelta(minutes=10)

        # Step 2: Fetch the latest 10 temperature records for the sensor within the time window
        temperature_records = self.repository.get_latest_by_sensor_id(sensor_id, start_time, limit=10)

        # Step 3: Fetch min and max temperature settings for the sensor
        settings = self.setting_repository.get_by_sensor_id(sensor_id)
        min_temperature = settings.min_temperature if settings else 0
        max_temperature = settings.max_temperature if settings else 100

        # Step 4: Format actual temperature data for chart display
        actual_temperature_data = [
            {"x": record.created_at.strftime("%H:%M"), "y": record.temperature}
            for record in temperature_records
        ]
        actual_temperature_data.reverse()  # Reverse the order so that the most recent appears last

        # Step 5: Generate chart data for min and max values (static over the time range)
        min_temperature_data = [
            {"x": (current_time - timedelta(minutes=i)).strftime("%H:%M"), "y": min_temperature}
            for i in range(10)
        ]
        min_temperature_data.reverse()  # Reverse the order for min temperature data

        max_temperature_data = [
            {"x": (current_time - timedelta(minutes=i)).strftime("%H:%M"), "y": max_temperature}
            for i in range(10)
        ]
        max_temperature_data.reverse()  # Reverse the order for max temperature data

        # Step 6: Build the full chart data combining min, actual, and max temperature values
        chart_data = [
            {"id": "Minimum", "color": "blue", "data": min_temperature_data},
            {"id": "Temperature", "color": "green", "data": actual_temperature_data},
            {"id": "Maximum", "color": "red", "data": max_temperature_data}
        ]

        return chart_data
