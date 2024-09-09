from ..models.sensor_model import SensorModel
from .base_repository import BaseRepository

class SensorRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(SensorModel, db_session)
