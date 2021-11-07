import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.beehive import BeehiveSearchResults, Beehive, BeehiveCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Beehive])
def fetch_beehives(*, db: Session = Depends(deps.get_db)) -> list:
    beehives = crud.beehive.get_multi(db=db)
    return beehives
