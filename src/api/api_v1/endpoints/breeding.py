import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.breeding import BreedingSearchResults, Breeding, BreedingCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Breeding])
def fetch_breedings(*, db: Session = Depends(deps.get_db)) -> list:
    breedings = crud.breeding.get_multi(db=db)
    return breedings
