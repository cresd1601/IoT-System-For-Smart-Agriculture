from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel

class SensorTypeModel(BaseModel):
    __tablename__ = 'sensor_types'

    type = Column(String(255), nullable=False)
    sensors = relationship('SensorModel', back_populates='type')
