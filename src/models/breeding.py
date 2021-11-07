from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Breeding(Base):
    id = Column(Integer, primary_key=True, index=True)
    lon = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)
