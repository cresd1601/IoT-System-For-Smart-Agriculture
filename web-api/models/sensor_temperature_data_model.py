from sqlalchemy import Column, Float, Integer, ForeignKey, DateTime
from .base_model import BaseModel

class SensorTemperatureDataModel(BaseModel):
    __tablename__ = 'sensor_temperature_data'

    sensor_id = Column(Integer, ForeignKey('sensors.id'), nullable=False)

    humidity = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
