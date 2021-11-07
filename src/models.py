from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from src.database import Base


# --------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    beehives = relationship("Beehive", back_populates="owner")


# --------------------------
class Beehive(Base):
    __tablename__ = "beehives"

    id = Column(Integer, primary_key=True, index=True)
    lon = Column(Float)
    lat = Column(Float)
    cluster_id = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    owner = relationship("User", back_populates="beehives")


# --------------------------
class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)
    start_lon = Column(Float)
    start_lat = Column(Float)
    end_lon = Column(Float)
    end_lat = Column(Float)


# --------------------------
class Disease(Base):
    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, index=True)
    lon = Column(Float)
    lat = Column(Float)
    radius = Column(Integer)
    is_active = Column(Boolean, default=True)
