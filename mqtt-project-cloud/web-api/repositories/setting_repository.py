from ..models.setting_model import SettingModel
from .base_repository import BaseRepository

class SettingRepository(BaseRepository):
    def __init__(self, db_session):
        super().__init__(SettingModel, db_session)

    def get_by_sensor_id(self, sensor_id):
        return self.db_session.query(self.model).filter_by(sensor_id=sensor_id).first()

    def update_by_sensor_id(self, sensor_id, update_data):
        setting = self.get_by_sensor_id(sensor_id)

        if setting:
            for key, value in update_data.items():
                setattr(setting, key, value)
            self.db_session.commit()
            return setting
        return None