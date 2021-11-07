from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Movement(Base):
    id = Column(Integer, primary_key=True, index=True)
    start_lon = Column(Float, nullable=False)
    start_lat = Column(Float, nullable=False)
    end_lon = Column(Float, nullable=False)
    end_lat = Column(Float, nullable=False)
    date = Column(String, nullable=False)
