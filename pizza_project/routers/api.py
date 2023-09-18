from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from auth.settings import auth_backend
from pizza_project.database import User
from pizza_project.routers import pizza_routers
from pizza_project.routers import users_routers
from pizza_project.schemas import UserRead, UserCreate, UserUpdate

api_router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_active_user = fastapi_users.current_user(active=True)


api_router.include_router(pizza_routers.router, tags=["pizza"])
api_router.include_router(users_routers.router, tags=["users"])
api_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
