from typing import List
from sqlalchemy.orm import Session

from . import models


def get_department_list(university: str, faculty: str, db: Session):
    objs: List[models.Department] = (
        db.query(models.Department)
        .filter_by(university=university, faculty=faculty)
        .all()
    )
    return objs
