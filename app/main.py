from fastapi import FastAPI

from app.auth import auth_router
from app.users import user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "PTNK-Library API was started! Now you can access the API at /docs"}
