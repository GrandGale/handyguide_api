from fastapi import FastAPI

from app.university.api import router as university_router
from app.faculty.api import router as faculty_router

app = FastAPI()


app.include_router(university_router, prefix="/university", tags=["university"])
app.include_router(faculty_router, prefix="/university/{university}/faculty", tags=["faculty"])
