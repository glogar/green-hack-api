import logging
from sqlalchemy.orm import Session

from src import crud, schemas
from src.db import base  # noqa: F401
# from src.recipe_data import RECIPES

logger = logging.getLogger(__name__)

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    if settings.FIRST_SUPERUSER_EMAIL:
        user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
        if not user:
            user_in = schemas.UserCreate(
                full_name="Initial Super User",
                email=settings.FIRST_SUPERUSER_EMAIL,
                phone=settings.FIRST_SUPERUSER_PHONE,
                is_superuser=True,
            )
            user = crud.user.create(db, obj_in=user_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{settings.FIRST_SUPERUSER_EMAIL} already exists. "
            )

    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER_EMAIL needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER_EMAIL=admin@api.coursemaker.io"
        )
