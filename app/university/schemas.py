from pydantic import BaseModel, Field


class BaseUniversity(BaseModel):
    name: str = Field(
        description="Name of the university",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the university",
        max_length=10,
    )


class UniversityCreate(BaseUniversity):
    pass


class University(BaseUniversity):
    pass

    class Config:
        orm_mode = True
