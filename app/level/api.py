from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.level import schemas, selectors, services

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Level)
def create_level(level: schemas.LevelCreate, db: Session = Depends(get_db)):
    return services.create_level(level=level, db=db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Level])
def get_level_list(db: Session = Depends(get_db)):
    return selectors.get_level_list(db=db)


@router.get("/{level}", status_code=status.HTTP_200_OK, response_model=schemas.Level)
def get_level(level: str, db: Session = Depends(get_db)):
    return selectors.get_level(level_abbrev=level, db=db)
