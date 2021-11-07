from pydantic import BaseModel

from typing import Sequence

from datetime import datetime


class DiseaseBase(BaseModel):
    lon: float
    lat: float
    radius: int
    start_date: str
    end_date: str
    is_active: bool


class DiseaseCreate(DiseaseBase):
    pass


class DiseaseUpdate(DiseaseBase):
    pass


# Properties shared by models stored in DB
class DiseaseInDBBase(DiseaseBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Disease(DiseaseInDBBase):
    pass


# Properties properties stored in DB
class DiseaseInDB(DiseaseInDBBase):
    pass


class DiseaseSearchResults(BaseModel):
    results: Sequence[Disease]
