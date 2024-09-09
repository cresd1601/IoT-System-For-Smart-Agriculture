from ..models.sensor_type_model import SensorTypeModel
from .base_repository import BaseRepository

class SensorTypeRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(SensorTypeModel, db_session)
