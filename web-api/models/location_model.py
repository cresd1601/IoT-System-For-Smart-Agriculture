from sqlalchemy import Column, String
from .base_model import BaseModel

class LocationModel(BaseModel):
    __tablename__ = 'locations'

    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
