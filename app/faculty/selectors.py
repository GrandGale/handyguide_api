from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from . import models


def get_faculty_list(university: str, db: Session = Depends(get_db)):
    objs: List[models.Faculty] = (
        db.query(models.Faculty).filter_by(university=university).all()
    )
    print(objs)
    return objs
