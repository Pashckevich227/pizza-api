from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}
