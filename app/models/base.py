from datetime import datetime
from pydantic import BaseModel


class BaseDetailModel(BaseModel):
    id: int
    name: str
    abbrev: str
    date_created: datetime
