from pydantic import BaseModel, Field


class BaseLevel(BaseModel):
    name: str = Field(
        description="Name of the level",
        max_length=100,
    )
    abbrev: str = Field(
        description="Abbreviation of the level",
        max_length=10,
    )


class LevelCreate(BaseLevel):
    pass


class Level(BaseLevel):
    pass
