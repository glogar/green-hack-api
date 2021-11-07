from src.crud.base import CRUDBase
from src.models.movement import Movement
from src.schemas.movement import MovementCreate, MovementUpdate


class CRUDMovement(CRUDBase[Movement, MovementCreate, MovementUpdate]):
    pass


movement = CRUDMovement(Movement)
