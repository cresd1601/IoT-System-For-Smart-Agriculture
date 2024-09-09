from sqlalchemy import Column, Float, Integer, ForeignKey, DateTime
from .base_model import BaseModel

class SensorMoistureDataModel(BaseModel):
    __tablename__ = 'sensor_moisture_data'

    sensor_id = Column(Integer, ForeignKey('sensors.id'), nullable=False)
    moisture = Column(Float, nullable=False)
