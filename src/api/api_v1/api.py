from fastapi import APIRouter

from src.api.api_v1.endpoints import user
from src.api.api_v1.endpoints import beehive
from src.api.api_v1.endpoints import beestand
from src.api.api_v1.endpoints import breeding
from src.api.api_v1.endpoints import disease
from src.api.api_v1.endpoints import movement


api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(beehive.router, prefix="/beehives", tags=["beehives"])
api_router.include_router(beestand.router, prefix="/beestands", tags=["beestands"])
api_router.include_router(breeding.router, prefix="/breedings", tags=["breedings"])
api_router.include_router(disease.router, prefix="/diseases", tags=["diseases"])
api_router.include_router(movement.router, prefix="/movements", tags=["movements"])
