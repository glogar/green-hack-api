from pydantic import BaseModel

from typing import Sequence


class BreedingBase(BaseModel):
    lon: float
    lat: float


class BreedingCreate(BreedingBase):
    pass


class BreedingUpdate(BreedingBase):
    pass


# Properties shared by models stored in DB
class BreedingInDBBase(BreedingBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Breeding(BreedingInDBBase):
    pass


# Properties properties stored in DB
class BreedingInDB(BreedingInDBBase):
    pass


class BreedingSearchResults(BaseModel):
    results: Sequence[Breeding]
