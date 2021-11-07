from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Disease(Base):
    id = Column(Integer, primary_key=True, index=True)
    lon = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)
    radius = Column(Integer, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
