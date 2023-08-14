import os
from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, "media/")


class Settings(BaseSettings):
    DEBUG: bool = os.environ.get("DEBUG")
    SESSION: str = os.environ.get("SESSION")

    # DB Settings
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")

    # Azure Settings
    AZURE_STORAGE_ACCOUNT_NAME: str = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")
    AZURE_STORAGE_ACCOUNT_KEY: str = os.environ.get("AZURE_STORAGE_ACCOUNT_KEY")
    AZURE_CONNECTION_STRING: str = os.environ.get("AZURE_CONNECTION_STRING")
    AZURE_CONTAINER_NAME: str = os.environ.get("AZURE_CONTAINER_NAME")
    AZURE_BLOB_URL: str = os.environ.get("AZURE_BLOB_URL")

    class Config:
        env_file = ".env"

    @property
    def POSTGRES_URL(self):
        url = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return url


settings = Settings()
