
from fastapi import APIRouter, Depends
from app.bookings.dao import BookingDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("/bookings")
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_by_id(user.id)


@router.delete("/bookings/{booking_id}")
async def del_bookings(booking_id: int, user: Users = Depends(get_current_user)):
    return await BookingDAO.delete(id = booking_id)

