import asyncio

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from src import crud
from src.api import deps

from src.schemas.beehive import BeehiveSearchResults, Beehive, BeehiveCreate

router = APIRouter()


@router.get("/", status_code=200, response_model=List[Beehive])
def fetch_beehives(
    *,
    skip: Optional[int] = 0,
    limit: Optional[int] = 500,
    db: Session = Depends(deps.get_db)
) -> list:
    beehives = crud.beehive.get_multi(db=db, skip=skip, limit=limit)
    return beehives


# @router.get("/search/", status_code=200, response_model=BeehiveSearchResults)
# def search_beehives(
#     *,
#     cluster_id: Optional[int] = None,
#     max_results: Optional[int] = 10,
#     db: Session = Depends(deps.get_db),
# ) -> dict:
#     """
#     Search for beehives based on cluster_id
#     """
#     beehives = crud.beehive.get_multi(db=db, limit=max_results)
#     results = filter(lambda beehive: cluster_id in beehive.cluster_id, beehives)

#     return {"results": list(results)}
