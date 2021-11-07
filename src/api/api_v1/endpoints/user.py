import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.user import User

router = APIRouter()


@router.get("/", status_code=200, response_model=List[User])
def fetch_users(*, db: Session = Depends(deps.get_db)) -> list:
    users = crud.user.get_multi(db=db)
    return users
