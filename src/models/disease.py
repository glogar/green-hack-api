from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Disease(Base):
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=False)
    lon = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)
    radius = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
