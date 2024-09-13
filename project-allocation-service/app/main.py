from fastapi import FastAPI
from app.routes import router
from app.database import connect_to_db

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_to_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to Project Management"}

app.include_router(router, prefix="/projects")