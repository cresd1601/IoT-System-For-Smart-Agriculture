from .base_service import BaseService
from ..repositories.sensor_repository import SensorRepository

class SensorService(BaseService):
    def __init__(self, repository: SensorRepository):
        super().__init__(repository)
