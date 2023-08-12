from fastapi import APIRouter

router = APIRouter()


@router.get("/pizza/{id}", tags=["pizza"])
async def read_user(id: int):
    return {"Pizza": id}