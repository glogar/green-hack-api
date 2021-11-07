from pydantic import BaseModel

from typing import Sequence


class DiseaseBase(BaseModel):
    label: str
    lon: float
    lat: float
    radius: int
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
