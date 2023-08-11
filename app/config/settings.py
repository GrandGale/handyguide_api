import os
from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, "media/")


class Settings(BaseSettings):
    DEBUG: bool
    SESSION: str
    SQLALCHEMY_DATABASE_URL: str
    AZURE_STORAGE_ACCOUNT_NAME: str
    AZURE_STORAGE_ACCOUNT_KEY: str
    AZURE_CONNECTION_STRING: str
    AZURE_CONTAINER_NAME: str
    AZURE_BLOB_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
