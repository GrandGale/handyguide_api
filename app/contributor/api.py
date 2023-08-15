from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session
from app.contributor import schemas, services
from app.department.validators import department_is_valid

from app.dependencies import get_db
from app.faculty.validators import faculty_is_valid
from app.level.validators import level_is_valid
from app.university.validators import university_is_valid

router = APIRouter()


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.Contributor,
)
def create_contributor(
    contributor: schemas.ContributorCreate, db: Session = Depends(get_db)
):
    university_is_valid(university_abbrev=contributor.university, db=db)
    level_is_valid(level_abbrev=contributor.level, db=db)
    faculty_is_valid(
        university=contributor.university, faculty_id=contributor.faculty, db=db
    )
    department_is_valid(
        university=contributor.university, department_id=contributor.department, db=db
    )
    return services.create_contributor(contributor=contributor, db=db)
