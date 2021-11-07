from pydantic import BaseModel

from typing import Sequence


class BeehiveBase(BaseModel):
    label: str
    lon: float
    lat: float
    cluster_id: int


class BeehiveCreate(BeehiveBase):
    owner_id: int


class BeehiveUpdate(BeehiveBase):
    owner_id: int


# Properties shared by models stored in DB
class BeehiveInDBBase(BeehiveBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Beehive(BeehiveInDBBase):
    pass


# Properties properties stored in DB
class BeehiveInDB(BeehiveInDBBase):
    pass


class BeehiveSearchResults(BaseModel):
    results: Sequence[Beehive]
