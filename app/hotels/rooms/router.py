from fastapi import APIRouter

from app.hotels.rooms.dao import RoomsDAO

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)

@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id):
    return await RoomsDAO.find_by_id_all(int(hotel_id))