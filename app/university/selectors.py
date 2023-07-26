from sqlalchemy.orm import Session

from .models import University


def get_university(db: Session, id: int):
    return db.query(University).filter(University.id == id).first()
