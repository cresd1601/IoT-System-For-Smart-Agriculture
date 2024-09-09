from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from ..models.sensor_moisture_data_model import SensorMoistureDataModel

class SensorMoistureDataRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_sensor_id(self, sensor_id):
        """Fetch all moisture data for a specific sensor."""
        return (
            self.session.query(SensorMoistureDataModel)
            .filter(SensorMoistureDataModel.sensor_id == sensor_id)
            .all()
        )

    def get_latest_by_sensor_id(self, sensor_id, start_time, limit=10):
        """Fetch one moisture data record per minute within the time window, limited to 10 results."""

        # Fetch the most recent record per minute
        subquery = (
            self.session.query(
                func.max(SensorMoistureDataModel.created_at).label('max_created_at')
            )
            .filter(SensorMoistureDataModel.sensor_id == sensor_id)
            .filter(SensorMoistureDataModel.created_at >= start_time)
            .group_by(func.date_format(SensorMoistureDataModel.created_at, '%Y-%m-%d %H:%i'))  # Group by minute
        ).subquery()

        # Join subquery to get the actual records for each minute
        result = (
            self.session.query(SensorMoistureDataModel)
            .join(subquery, SensorMoistureDataModel.created_at == subquery.c.max_created_at)
            .order_by(desc(SensorMoistureDataModel.created_at))  # Order by latest
            .limit(limit)
            .all()
        )

        return result