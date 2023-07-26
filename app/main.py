from fastapi import FastAPI

from .university import api

app = FastAPI()


app.include_router(api.router, prefix="/university", tags=["university"])
