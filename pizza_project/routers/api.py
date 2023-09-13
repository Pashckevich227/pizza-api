from fastapi import APIRouter
from pizza_project.routers import pizza_routers
from pizza_project.routers import users_routers

api_router = APIRouter()

api_router.include_router(pizza_routers.router, tags=["pizza"])
api_router.include_router(users_routers.router, tags=["users"])

