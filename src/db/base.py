# Import all the models, so that Base has them before being
# imported by Alembic
from src.db.base_class import Base  # noqa
from src.models.user import User  # noqa
from src.models.beehive import Beehive  # noqa
from src.models.beestand import Beestand  # noqa
from src.models.breeding import Breeding  # noqa
from src.models.movement import Movement  # noqa
from src.models.disease import Disease  # noqa
