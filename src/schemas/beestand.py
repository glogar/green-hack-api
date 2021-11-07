from pydantic import BaseModel

from typing import Sequence


class BeestandBase(BaseModel):
    lon: float
    lat: float
    occupancy: float


class BeestandCreate(BeestandBase):
    pass


class BeestandUpdate(BeestandBase):
    pass


# Properties shared by models stored in DB
class BeestandInDBBase(BeestandBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Beestand(BeestandInDBBase):
    pass


# Properties properties stored in DB
class BeestandInDB(BeestandInDBBase):
    pass


class BeestandSearchResults(BaseModel):
    results: Sequence[Beestand]
