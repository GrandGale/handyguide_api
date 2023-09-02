from fastapi import Query, UploadFile, status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.course.validators import course_is_valid
from app.department.validators import department_is_valid
from app.faculty.validators import faculty_is_valid
from app.handout import selectors, services, schemas
from app.dependencies import get_db
from app.handout.validators import handout_id_is_valid
from app.level.validators import level_is_valid
from app.university.validators import university_is_valid

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Handout)
def create_handout(
    university: str,
    handout: schemas.HandoutCreate,
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    course_is_valid(university=university, course_id=handout.course, db=db)
    return services.create_handout(university=university, handout=handout, db=db)


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Handout
)
async def upload_handout(id: int, file: UploadFile, db: Session = Depends(get_db)):
    handout_id_is_valid(id=id, db=db)
    obj = await services.upload_handout(id=id, file=file, db=db)
    return obj


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=schemas.PaginatedHandout
)
def get_handout_list(
    university: str | None = None,
    faculty: int | None = None,
    department: int | None = None,
    course: int | None = None,
    level: str | None = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    faculty_is_valid(university=university, faculty_id=faculty, db=db)
    department_is_valid(university=university, department_id=department, db=db)
    course_is_valid(university=university, course_id=course, db=db)
    level_is_valid(level_abbrev=level, db=db)
    return selectors.get_handout_list(
        university=university,
        faculty=faculty,
        department=department,
        course=course,
        level=level,
        page=page,
        size=size,
        db=db,
    )


@router.get(
    "/search/", status_code=status.HTTP_200_OK, response_model=schemas.PaginatedHandout
)
def handout_search(
    q: str,
    university: str | None = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, le=50),
    db: Session = Depends(get_db),
):
    university_is_valid(university_abbrev=university, db=db)
    return selectors.handout_search(
        q=q, university=university, page=page, size=size, db=db
    )
