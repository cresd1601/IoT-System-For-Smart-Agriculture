from .base_service import BaseService
from ..repositories.sensor_type_repository import SensorTypeRepository

class SensorTypeService(BaseService):
    def __init__(self, repository: SensorTypeRepository):
        super().__init__(repository)
