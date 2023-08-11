from pydantic import BaseModel


class UserBase(BaseModel):
    city: str
    street: str
    house: str
    floor: int
    room: int


class UserCreate(UserBase):
    name: str
    telephone: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class PizzaBase(BaseModel):
    size: str
    price: float


class PizzaCreate(BaseModel):
    name: str
    description: str


class Pizza(PizzaBase):
    id: int

    class Config:
        orm_mode = True
