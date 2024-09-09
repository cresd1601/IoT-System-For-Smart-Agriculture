from .base_service import BaseService
from ..repositories.sensor_temperature_data_repository import SensorTemperatureDataRepository

class SensorTemperatureDataService(BaseService):
    def __init__(self, repository: SensorTemperatureDataRepository):
        super().__init__(repository)
