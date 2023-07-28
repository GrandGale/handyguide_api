from fastapi import FastAPI

from app.university.api import router as university_router
from app.faculty.api import router as faculty_router
from app.department.api import router as department_router
from app.level.api import router as level_router
from app.course.api import router as course_router

app = FastAPI()


app.include_router(university_router, prefix="/university", tags=["university"])
app.include_router(level_router, prefix="/level", tags=["level"])
app.include_router(
    faculty_router, prefix="/university/{university}/faculty", tags=["faculty"]
)
app.include_router(
    department_router,
    prefix="/university/{university}/department",
    tags=["department"],
)
app.include_router(course_router, prefix="/university/{university}/course")
