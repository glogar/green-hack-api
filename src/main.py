from typing import List

from fastapi import Depends, FastAPI, APIRouter, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Apisearch (Green Hack)", openapi_url="/openapi.json"
)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/beehives/", response_model=schemas.Beehive)
def create_item_for_user(
        user_id: int,
        item: schemas.BeehiveCreate,
        db: Session = Depends(get_db)
    ):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/beehives/", response_model=List[schemas.Beehive])
def read_beehives(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    beehives = crud.get_beehives(db, skip=skip, limit=limit)
    return beehives


@router.get("/movements/", response_model=List[schemas.Movement])
def read_movements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movements = crud.get_movements(db, skip=skip, limit=limit)
    return movements


@router.get("/diseases/", response_model=List[schemas.Disease])
def read_diseases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diseases = crud.get_diseases(db, skip=skip, limit=limit)
    return diseases


app.include_router(router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
