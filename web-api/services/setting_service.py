from .base_service import BaseService
from ..repositories.setting_repository import SettingRepository

class SettingService(BaseService):
    def __init__(self, repository: SettingRepository):
        super().__init__(repository)
