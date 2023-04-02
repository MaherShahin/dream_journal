import uvicorn
from fastapi import FastAPI, Depends
from backend.app import models
from backend.app.utils.database import Base, db
from backend.app.routers import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.on_event("startup")
async def startup():
    # Create the database tables
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    
