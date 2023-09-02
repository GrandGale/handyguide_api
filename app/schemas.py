from pydantic import BaseModel, Field


class PaginatedResponse(BaseModel):
    page: int = Field(description="The current page")
    size: int = Field(description="The number of items per page")
    count: int = Field(description="The number of items returned")
