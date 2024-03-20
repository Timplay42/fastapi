from app.dao.base import DAO
from app.bookings.models import Bookings

class BookingDAO(DAO):
    model = Bookings
