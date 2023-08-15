from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

router = APIRouter()
