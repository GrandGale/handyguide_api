from pydantic import BaseModel, Field


class BaseHandout(BaseModel):
    title: str = Field(description="The Title of the handout", max_length=100)
    course: str = Field(description="The Course of the handout", max_length=10)


class HandoutCreate(BaseHandout):
    faculty: str = Field(description="The Faculty of the handout", max_length=10)
    department: str = Field(description="The Department of the handout", max_length=10)

class Handout(BaseHandout):
    id: int
    url: str
    university: str 
