from fastapi import Depends
from pizza_project.routers.api import current_active_user
from pizza_project.main import app
from pizza_project.models import User


