from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel

class SensorModel(BaseModel):
    __tablename__ = 'sensors'

    name = Column(String(255), nullable=False)

    type_id = Column(Integer, ForeignKey('sensor_types.id'))
    type = relationship('SensorTypeModel', back_populates='sensors')

    location_id = Column(Integer, ForeignKey('locations.id'), nullable=True)
    location = relationship('LocationModel')

