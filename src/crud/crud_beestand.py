from src.crud.base import CRUDBase
from src.models.beestand import Beestand
from src.schemas.beestand import BeestandCreate, BeestandUpdate


class CRUDBeestand(CRUDBase[Beestand, BeestandCreate, BeestandUpdate]):
    pass


beestand = CRUDBeestand(Beestand)
