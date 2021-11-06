from sqlalchemy.orm import Session

from . import models, schemas

# --------------------------
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = "fake__" + user.password + "__letmein"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# --------------------------
def get_beehives(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Beehive).offset(skip).limit(limit).all()


def create_user_beehive(db: Session, item: schemas.BeehiveCreate, user_id: int):
    db_beehive = models.Beehive(**item.dict(), owner_id=user_id)
    db.add(db_beehive)
    db.commit()
    db.refresh(db_beehive)
    return db_beehive


# --------------------------
def get_movements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movement).offset(skip).limit(limit).all()


# --------------------------
def get_diseases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Disease).offset(skip).limit(limit).all()
