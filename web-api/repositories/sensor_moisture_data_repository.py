from ..models.sensor_moisture_data_model import SensorMoistureDataModel
from .base_repository import BaseRepository

class SensorMoistureDataRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(SensorMoistureDataModel, db_session)

    def get_by_sensor_id(self, sensor_id):
        return self.db_session.query(SensorMoistureDataModel).filter_by(sensor_id=sensor_id).all()
