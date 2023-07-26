from sqlalchemy.orm import Session

from .models import University


def university_exists(db: Session, university: University):
    return (
        db.query(University)
        .filter(
            University.name == university.name, University.abbrev == university.abbrev
        )
        .first()
        is not None
    )
