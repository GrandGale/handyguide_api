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
    level: str = Field(description="The level Abbrev of the course", max_length=10)


class CourseCreate(BaseCourse):
    department: int
    faculty: int


class Course(BaseCourse):
    id: int
    university: str


class CourseDetail(BaseCourse):
    id: int
    department: int
    faculty: int
    university: str
