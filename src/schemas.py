from typing import List, Optional
from pydantic import BaseModel


# --------------------------
class BeehiveBase(BaseModel):
    lon: float
    lat: float


class BeehiveCreate(BeehiveBase):
    pass


class Beehive(BeehiveBase):
    id: int
    cluster_id: int
    owner_id: int

    class Config:
        orm_mode = True


# --------------------------
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    beehives: List[Beehive] = []

    class Config:
        orm_mode = True


# --------------------------
class MovementBase(BaseModel):
    start_lon: float
    start_lat: float
    end_lon: float
    end_lat: float


class MovementCreate(MovementBase):
    pass


class Movement(MovementBase):
    id: int

    class Config:
        orm_mode = True


# --------------------------
class DiseaseBase(BaseModel):
    lon: float
    lat: float


class DiseaseCreate(DiseaseBase):
    radius: int


class Disease(DiseaseBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
