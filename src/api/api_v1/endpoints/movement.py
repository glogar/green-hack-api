import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.movement import MovementSearchResults, Movement, MovementCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Movement])
def fetch_movements(
    *,
    skip: Optional[int] = 0,
    limit: Optional[int] = 1000,
    db: Session = Depends(deps.get_db)
) -> list:
    movements = crud.movement.get_multi(db=db, skip=skip, limit=limit)
    return movements
