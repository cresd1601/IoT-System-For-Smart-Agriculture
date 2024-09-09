from sqlalchemy import Column, Integer, Float, ForeignKey
from .base_model import BaseModel

class SettingModel(BaseModel):
    __tablename__ = 'settings'

    sensor_id = Column(Integer, ForeignKey('sensors.id'), nullable=False)
    
    max_temperature = Column(Float, nullable=True)
    min_temperature = Column(Float, nullable=True)
    max_humidity = Column(Float, nullable=True)
    min_humidity = Column(Float, nullable=True)
    max_moisture = Column(Float, nullable=True)
    min_moisture = Column(Float, nullable=True)
