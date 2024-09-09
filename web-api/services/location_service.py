from .base_service import BaseService
from ..repositories.location_repository import LocationRepository

class LocationService(BaseService):
    def __init__(self, repository: LocationRepository):
        super().__init__(repository)
