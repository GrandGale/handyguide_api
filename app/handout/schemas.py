from pydantic import BaseModel, Field

from app.schemas import PaginatedResponse


class BaseHandout(BaseModel):
    title: str = Field(description="The Title of the handout", max_length=100)
    course: int = Field(description="The Course ID of the handout")
    level: str = Field(description="The Level of the handout", max_length=10)


class HandoutCreate(BaseHandout):
    faculty: int = Field(description="The Faculty ID of the handout")
    department: int = Field(description="The Department ID of the handout")


class Handout(BaseHandout):
    id: int
    url: str
    university: str


class PaginatedHandout(PaginatedResponse):
    items: list[Handout] = Field(description="The list of handouts")
