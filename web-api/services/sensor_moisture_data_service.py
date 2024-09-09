from .base_service import BaseService
from ..repositories.sensor_moisture_data_repository import SensorMoistureDataRepository

class SensorMoistureDataService(BaseService):
    def __init__(self, repository: SensorMoistureDataRepository):
        super().__init__(repository)
