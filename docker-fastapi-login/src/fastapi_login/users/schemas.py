from typing import Union
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str


class UserDefault(object):
    email: str
    password: str
