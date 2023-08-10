import os
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    SESSION: str = "2022_2023"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///db.sqlite3"
    BASE_DIR: str = str(Path(__name__).resolve().parent)
    MEDIA_DIR: str = os.path.join(BASE_DIR, "media")


settings = Settings()
