from pydantic import BaseModel, Field


class DepartmentBase(BaseModel):
    name: str = Field(
        description="Name of the department",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the department",
        max_length=10,
    )


class DepartmentCreate(DepartmentBase):
    faculty: str


class Department(DepartmentBase):
    university: str
    faculty: str
