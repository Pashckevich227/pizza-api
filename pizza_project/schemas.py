import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    telephone: str = None
    email: EmailStr
    registered_at: datetime.datetime
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    telephone: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    username: str = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    telephone: str = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None


class PizzaCreate(BaseModel):
    name: str
    description: str
    size: str
    price: float


class Pizza(PizzaCreate):
    id: int

    class Config:
        orm_mode = True
