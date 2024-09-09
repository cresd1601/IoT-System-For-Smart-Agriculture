from ..models.setting_model import SettingModel
from .base_repository import BaseRepository

class SettingRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(SettingModel, db_session)

    def get_all_by_filter(self, **filters):
        return self.db_session.query(self.model).filter_by(**filters).all()
