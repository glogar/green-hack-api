from src.crud.base import CRUDBase
from src.models.beehive import Beehive
from src.schemas.beehive import BeehiveCreate, BeehiveUpdate


class CRUDBeehive(CRUDBase[Beehive, BeehiveCreate, BeehiveUpdate]):
    pass


beehive = CRUDBeehive(Beehive)
