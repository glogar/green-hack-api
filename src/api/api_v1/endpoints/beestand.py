import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.beestand import BeestandSearchResults, Beestand, BeestandCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Beestand])
def fetch_beestands(
    *,
    skip: Optional[int] = 0,
    limit: Optional[int] = 200,
    db: Session = Depends(deps.get_db)
) -> list:
    beestands = crud.beestand.get_multi(db=db, skip=skip, limit=limit)
    return beestands
