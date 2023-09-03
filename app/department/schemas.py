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


class DepartmentUpdate(BaseModel):
    name: str | None = None
    abbrev: str | None = None


class DepartmentCreate(DepartmentBase):
    faculty: int


class Department(DepartmentBase):
    id: int
    university: str
    faculty: int
