from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app import models, schemas
from backend.app.utils import security
from backend.app.utils.database import db

router = APIRouter()

@router.post("/register")
async def register(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = security.get_password_hash(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users")
async def get_users(db: Session = Depends(db.get_db)):
    users = db.query(models.User).all()
    return users
