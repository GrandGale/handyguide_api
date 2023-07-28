from pydantic import BaseModel, Field


class BaseCourse(BaseModel):
    name: str = Field(
        description="Name of the faculty",
        max_length=100,
    )
    code: str = Field(
        description="Abbreviation of the faculty",
        max_length=10,
    )
    level: str = Field(description="The level of the course", max_length=10)


class CourseCreate(BaseCourse):
    department: str
    faculty: str


class Course(BaseCourse):
    university: str


class CourseDetail(BaseCourse):
    department: str
    faculty: str
    university: str
