from pydantic import BaseModel, Field


class FacultyBase(BaseModel):
    name: str = Field(
        description="Name of the faculty",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the faculty",
        max_length=10,
    )


class FacultyUpdate(BaseModel):
    name: str | None = None
    abbrev: str | None = None


class FacultyCreate(FacultyBase):
    pass


class Faculty(FacultyBase):
    id: int
    university: str
