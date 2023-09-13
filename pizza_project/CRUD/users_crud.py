from typing import Annotated
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from pizza_project import models
from fastapi import HTTPException, status, Depends
from auth.user_auth import (verify_password,
                            oauth2_scheme)
from config import SECRET_KEY, ALGORITHM
from pizza_project.database import get_db
from pizza_project.schemas import TokenData, User


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_all_users(db: Session):
    return db.query(models.User).all()


def get_authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username=username)
    if not user:
        print({"msg": "User not found"})
        return {"msg": "User not found"}
    if not verify_password(password, user.password):
        print({"msg": "Password is not verify"})
        return {"msg": "Password is not verify"}
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
                           db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return current_user
