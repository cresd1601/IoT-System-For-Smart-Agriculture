from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..models.sensor_temperature_data_model import SensorTemperatureDataModel

class SensorTemperatureDataRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_sensor_id(self, sensor_id):
        """Fetch all temperature data for a specific sensor."""
        return (
            self.session.query(SensorTemperatureDataModel)
            .filter(SensorTemperatureDataModel.sensor_id == sensor_id)
            .all()
        )

    def get_latest_by_sensor_id(self, sensor_id, start_time, limit=10):
        """Fetch one temperature data record per minute within the time window, limited to 10 results."""

        # Fetch the most recent record per minute
        subquery = (
            self.session.query(
                func.max(SensorTemperatureDataModel.created_at).label('max_created_at')
            )
            .filter(SensorTemperatureDataModel.sensor_id == sensor_id)
            .filter(SensorTemperatureDataModel.created_at >= start_time)
            .group_by(func.date_format(SensorTemperatureDataModel.created_at, '%Y-%m-%d %H:%i'))  # Group by minute
        ).subquery()

        # Join subquery to get the actual records for each minute
        result = (
            self.session.query(SensorTemperatureDataModel)
            .join(subquery, SensorTemperatureDataModel.created_at == subquery.c.max_created_at)
            .order_by(desc(SensorTemperatureDataModel.created_at))  # Order by latest
            .limit(limit)
            .all()
        )

        return result
