from src.crud.base import CRUDBase
from src.models.breeding import Breeding
from src.schemas.breeding import BreedingCreate, BreedingUpdate


class CRUDBreeding(CRUDBase[Breeding, BreedingCreate, BreedingUpdate]):
    pass


breeding = CRUDBreeding(Breeding)
