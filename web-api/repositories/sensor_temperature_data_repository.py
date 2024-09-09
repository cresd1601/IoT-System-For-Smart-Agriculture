from ..models.sensor_temperature_data_model import SensorTemperatureDataModel
from .base_repository import BaseRepository

class SensorTemperatureDataRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(SensorTemperatureDataModel, db_session)

    def get_by_sensor_id(self, sensor_id):
        return self.db_session.query(SensorTemperatureDataModel).filter_by(sensor_id=sensor_id).all()