from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class Beehive(Base):
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(256), nullable=True)
    lon = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)
    cluster_id = Column(Integer, nullable=True)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    owner = relationship("User", back_populates="beehives")
