from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class DreamEntryBase(BaseModel):
    title: str
    content: str
    date: Optional[str] = None

class DreamEntryCreate(DreamEntryBase):
    pass

class DreamEntry(DreamEntryBase):
    id: int
    user_id: int

class Config:
    orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
