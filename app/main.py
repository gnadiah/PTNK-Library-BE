from fastapi import FastAPI

from app.auth import auth_router

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "PTNK-Library API was started! Now you can access the API at /docs"}
