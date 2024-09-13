from motor.motor_asyncio import AsyncIOMotorClient
import os

client = None
db = None

async def connect_to_db():
    global client, db
    MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")  # Use default URL if not provided
    client = AsyncIOMotorClient(MONGO_URL)
    db = client["employee_db"]

def get_employee_collection():
    return db["employees"]
