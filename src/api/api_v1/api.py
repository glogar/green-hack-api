from fastapi import APIRouter

from src.api.api_v1.endpoints import beehive


api_router = APIRouter()
api_router.include_router(beehive.router, prefix="/beehives", tags=["beehives"])
