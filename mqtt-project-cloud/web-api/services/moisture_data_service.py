from datetime import datetime, timedelta
from ..repositories.sensor_moisture_data_repository import SensorMoistureDataRepository
from ..repositories.sensor_repository import SensorRepository
from ..repositories.location_repository import LocationRepository
from ..repositories.setting_repository import SettingRepository

class MoistureDataService:
    def __init__(self,
                 moisture_data_repository: SensorMoistureDataRepository,
                 sensor_repository: SensorRepository,
                 location_repository: LocationRepository,
                 setting_repository: SettingRepository):
        self.repository = moisture_data_repository
        self.sensor_repository = sensor_repository
        self.location_repository = location_repository
        self.setting_repository = setting_repository

    def get_all_data_by_sensor_id(self, sensor_id):
        """Fetch detailed moisture data for the specific sensor_id."""
        moisture_data = self.repository.get_by_sensor_id(sensor_id)
        detailed_data = []

        if not moisture_data:
            return detailed_data  # Return empty list if no data

        sensor = self.sensor_repository.get_by_id(sensor_id)
        location = self.location_repository.get_by_id(sensor.location_id) if sensor else None

        for data in moisture_data:
            detailed_data.append({
                'id': data.id,
                'date_time': data.created_at,
                'sensor_name': sensor.name if sensor else 'Unknown Sensor',
                'location': location.name if location else 'Unknown Location',
                'moisture': data.moisture
            })

        return detailed_data

    def get_chart_data_by_sensor_id(self, sensor_id):
        """Fetch the latest 10 moisture records from the last 10 minutes for chart data,
        and include min and max moisture levels."""

        current_time = datetime.utcnow()
        start_time = current_time - timedelta(minutes=10)

        # Step 1: Fetch the latest 10 moisture records for the sensor within the time window
        moisture_records = self.repository.get_latest_by_sensor_id(sensor_id, start_time, limit=10)

        # Step 2: Fetch min and max moisture settings for the sensor
        settings = self.setting_repository.get_by_sensor_id(sensor_id)
        min_moisture = settings.min_moisture if settings else 0
        max_moisture = settings.max_moisture if settings else 100

        # Step 3: Format actual moisture data for chart display
        actual_moisture_data = [
            {"x": record.created_at.strftime("%H:%M"), "y": record.moisture}
            for record in moisture_records
        ]
        actual_moisture_data.reverse()  # Reverse the data to show the most recent on the right

        # Step 4: Generate chart data for min and max values (static over the time range)
        min_moisture_data = [
            {"x": (current_time - timedelta(minutes=i)).strftime("%H:%M"), "y": min_moisture}
            for i in range(10)
        ]
        min_moisture_data.reverse()  # Reverse the data to align with reversed moisture data

        max_moisture_data = [
            {"x": (current_time - timedelta(minutes=i)).strftime("%H:%M"), "y": max_moisture}
            for i in range(10)
        ]
        max_moisture_data.reverse()  # Reverse the data to align with reversed moisture data

        # Step 5: Build the full chart data combining min, actual, and max moisture values
        chart_data = [
            {"id": "Minimum", "color": "blue", "data": min_moisture_data},
            {"id": "Moisture", "color": "green", "data": actual_moisture_data},
            {"id": "Maximum", "color": "red", "data": max_moisture_data}
        ]

        return chart_data
