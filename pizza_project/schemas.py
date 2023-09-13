from pydantic import (BaseModel,
                      EmailStr)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class TestUser(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class PizzaCreate(BaseModel):
    name: str
    description: str
    size: str
    price: float


class Pizza(PizzaCreate):
    id: int

    class Config:
        orm_mode = True
