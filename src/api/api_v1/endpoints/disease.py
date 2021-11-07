import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.disease import DiseaseSearchResults, Disease, DiseaseCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Disease])
def fetch_diseases(*, db: Session = Depends(deps.get_db)) -> list:
    diseases = crud.disease.get_multi(db=db)
    return diseases
