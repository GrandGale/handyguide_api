from pydantic import BaseModel, Field


class BaseContributor(BaseModel):
    username: str = Field(
        description="The Contributor's username", min_length=3, max_length=50
    )
    email: str = Field(description="The Contributor's email address", max_length=255)
    first_name: str = Field(description="The Contributor's first name", max_length=50)
    last_name: str = Field(description="The Contributor's last name", max_length=50)
    university_id: str = Field(
        description="The Contributor's university ID", max_length=50
    )
    university: str = Field(description="The Contributor's university", max_length=50)
    level: str = Field(description="The Contributor's level", max_length=50)
    faculty: int = Field(description="The Contributor's faculty")
    department: int = Field(description="The Contributor's department")


class ContributorCreate(BaseContributor):
    password: str


class Contributor(BaseContributor):
    is_contributor: bool
    is_supervisor: bool
    is_admin: bool
