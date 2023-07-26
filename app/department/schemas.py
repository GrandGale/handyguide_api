from pydantic import BaseModel, Field


class DepartmentBase(BaseModel):
    name: str = Field(
        description="Name of the faculty",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the faculty",
        max_length=10,
    )


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):
    university: str
    faculty: str