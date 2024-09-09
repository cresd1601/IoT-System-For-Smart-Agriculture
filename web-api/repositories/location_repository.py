from ..models.location_model import LocationModel
from .base_repository import BaseRepository

class LocationRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(LocationModel, db_session)
