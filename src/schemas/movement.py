from pydantic import BaseModel

from typing import Sequence


class MovementBase(BaseModel):
    start_lon: float
    start_lat: float
    end_lon: float
    end_lat: float


class MovementCreate(MovementBase):
    pass


class MovementUpdate(MovementBase):
    pass


# Properties shared by models stored in DB
class MovementInDBBase(MovementBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Movement(MovementInDBBase):
    pass


# Properties properties stored in DB
class MovementInDB(MovementInDBBase):
    pass


class MovementSearchResults(BaseModel):
    results: Sequence[Movement]
