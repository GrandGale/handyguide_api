from datetime import datetime
from pydantic import BaseModel, Extra, Field


class UniversityCreate(BaseModel):
    name: str = Field(
        description="Name of the university",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the university",
        max_length=10,
    )


class University(BaseModel):
    id: int = Field(description="Unique identifier for the university")
    name: str = Field(
        description="Name of the university",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the university",
        max_length=10,
    )

    class Config:
        orm_mode = True
