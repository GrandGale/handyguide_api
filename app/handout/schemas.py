from fastapi import UploadFile
from pydantic import BaseModel, Field


class BaseHandout(BaseModel):
    title: str = Field(description="The Title of the handout", max_length=100)
    course: str = Field(description="The Course of the handout", max_length=10)


class HandoutUpload(BaseHandout):
    file: UploadFile


class HandoutCreate(BaseHandout):
    pass


class Handout(BaseHandout):
    id: int
    url: str
