from ..models.setting_model import SettingModel  # Import the SettingModel
from ..repositories.setting_repository import SettingRepository  # Import the SettingRepository

class SettingService:
    def __init__(self, setting_repository: SettingRepository):
        self.setting_repository = setting_repository

    def get_all(self):
        settings = self.setting_repository.get_all()
        return [
            {
                'id': setting.id,
                'sensor_id': setting.sensor_id,
                'max_temperature': setting.max_temperature,
                'min_temperature': setting.min_temperature,
                'max_humidity': setting.max_humidity,
                'min_humidity': setting.min_humidity,
                'max_moisture': setting.max_moisture,
                'min_moisture': setting.min_moisture
            } for setting in settings
        ]

    def create(self, setting_data):
        new_setting = SettingModel(
            sensor_id=setting_data.get("sensor_id"),
            max_temperature=setting_data.get("max_temperature"),
            min_temperature=setting_data.get("min_temperature"),
            max_humidity=setting_data.get("max_humidity"),
            min_humidity=setting_data.get("min_humidity"),
            max_moisture=setting_data.get("max_moisture"),
            min_moisture=setting_data.get("min_moisture")
        )
        created_setting = self.setting_repository.create(new_setting)
        return {
            'id': created_setting.id,
            'sensor_id': created_setting.sensor_id,
            'max_temperature': created_setting.max_temperature,
            'min_temperature': created_setting.min_temperature,
            'max_humidity': created_setting.max_humidity,
            'min_humidity': created_setting.min_humidity,
            'max_moisture': created_setting.max_moisture,
            'min_moisture': created_setting.min_moisture
        }

    def delete(self, setting_id):
        return self.setting_repository.delete(setting_id)

    def get_by_sensor_id(self, sensor_id):
        setting = self.setting_repository.get_by_sensor_id(sensor_id)

        if setting:
            return {
                'id': setting.id,
                'sensor_id': setting.sensor_id,
                'max_temperature': setting.max_temperature,
                'min_temperature': setting.min_temperature,
                'max_humidity': setting.max_humidity,
                'min_humidity': setting.min_humidity,
                'max_moisture': setting.max_moisture,
                'min_moisture': setting.min_moisture
            }
        return None

    def update_by_sensor_id(self, sensor_id, setting_data):
        updated_setting = self.setting_repository.update_by_sensor_id(sensor_id, setting_data)

        if updated_setting:
            return {
                'id': updated_setting.id,
                'sensor_id': updated_setting.sensor_id,
                'max_temperature': updated_setting.max_temperature,
                'min_temperature': updated_setting.min_temperature,
                'max_humidity': updated_setting.max_humidity,
                'min_humidity': updated_setting.min_humidity,
                'max_moisture': updated_setting.max_moisture,
                'min_moisture': updated_setting.min_moisture
            }
        return None