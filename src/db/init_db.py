import logging
import json
from datetime import datetime
from sqlalchemy.orm import Session
from tqdm import tqdm

from src import crud, schemas
from src.db import base  # noqa: F401
from src.core.config import settings

# from src.recipe_data import RECIPES

logger = logging.getLogger(__name__)

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


f_beehive = open('src/db/initial_data/beehive.json')
f_beestand = open('src/db/initial_data/beestand.json')
f_breeding = open('src/db/initial_data/breeding.json')
f_disease = open('src/db/initial_data/disease.json')
f_movement = open('src/db/initial_data/movement.json')

DATA_BEEHIVE = json.loads(f_beehive.read())
DATA_BEESTAND = json.loads(f_beestand.read())
DATA_BREEDING = json.loads(f_breeding.read())
DATA_DISEASE = json.loads(f_disease.read())
DATA_MOVEMENT = json.loads(f_movement.read())

f_beehive.close()
# f_beestand.close()
f_breeding.close()
# f_disease.close()
# f_movement.close()

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

        # --------------------------------------
        if DATA_BEEHIVE:
            logger.info(
                "Importing DATA_BEEHIVE"
            )
            for beehive in tqdm(DATA_BEEHIVE):
                beehive_in = schemas.BeehiveCreate(
                    lon=beehive["lon"],
                    lat=beehive["lat"],
                    cluster_id=beehive["cluster_id"],
                    owner_id=beehive["owner_id"],
                )
                crud.beehive.create(db, obj_in=beehive_in)
        else:
            logger.warning(
                "Skipping creating DATA_BEEHIVE."
            )

        # --------------------------------------
        if DATA_BEESTAND:
            logger.info(
                "Importing DATA_BEESTAND"
            )
            for beestand in tqdm(DATA_BEESTAND):
                beestand_in = schemas.BeestandCreate(
                    lon=beestand["lon"],
                    lat=beestand["lat"],
                    occupancy=beestand["occupancy"],
                )
                crud.beestand.create(db, obj_in=beestand_in)
        else:
            logger.warning(
                "Skipping creating DATA_BEESTAND."
            )

        # --------------------------------------
        if DATA_BREEDING:
            logger.info(
                "Importing DATA_BREEDING"
            )
            for breeding in tqdm(DATA_BREEDING):
                breeding_in = schemas.BreedingCreate(
                    lon=breeding["lon"],
                    lat=breeding["lat"],
                )
                crud.breeding.create(db, obj_in=breeding_in)
        else:
            logger.warning(
                "Skipping creating DATA_BREEDING."
            )

        # --------------------------------------
        if DATA_DISEASE:
            logger.info(
                "Importing DATA_DISEASE"
            )
            for disease in tqdm(DATA_DISEASE):
                start_date = datetime.strptime(disease["start_date"], "%Y-%m-%d")
                str_start_date = start_date.strftime("%Y-%m-%d %H:%M:%S.00000")

                if disease["end_date"] != "NaT":
                    end_date = datetime.strptime(disease["end_date"], "%Y-%m-%d")
                    str_end_date = start_date.strftime("%Y-%m-%d %H:%M:%S.00000")
                else:
                    str_end_date = ""

                disease_in = schemas.DiseaseCreate(
                    lon=disease["lon"],
                    lat=disease["lat"],
                    radius=disease["radius"],
                    start_date=str_start_date,
                    end_date=str_end_date,
                    is_active=disease["is_active"],
                )
                crud.disease.create(db, obj_in=disease_in)
        else:
            logger.warning(
                "Skipping creating DATA_DISEASE."
            )

        # --------------------------------------
        if DATA_MOVEMENT:
            logger.info(
                "Importing DATA_MOVEMENT"
            )
            for movement in tqdm(DATA_MOVEMENT):
                date = datetime.strptime(movement["date"], "%Y-%m-%d")

                movement_in = schemas.MovementCreate(
                    start_lon=movement["start_lon"],
                    start_lat=movement["start_lat"],
                    end_lon=movement["end_lon"],
                    end_lat=movement["end_lat"],
                    date=date.strftime("%Y-%m-%d %H:%M:%S.00000"),
                )
                crud.movement.create(db, obj_in=movement_in)
        else:
            logger.warning(
                "Skipping creating DATA_MOVEMENT."
            )

    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER_EMAIL needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER_EMAIL=admin@api.coursemaker.io"
        )
