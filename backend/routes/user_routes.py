from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["Usuario"])

@router.get("/")
async def list_user():
    return "usuario"