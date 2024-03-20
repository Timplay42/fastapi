from fastapi import APIRouter

from app.hotels.dao import HotelsDAO

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("/{location}")
async def get_hotels(location: str):
    return await HotelsDAO.find_by_location(location)