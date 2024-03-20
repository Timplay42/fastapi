from app.dao.base import DAO
from app.hotels.models import Hotels
from app.database import async_session_maker

from sqlalchemy import select

class HotelsDAO(DAO):
    model = Hotels


    @classmethod
    async def find_by_location(cls, location: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(location = location).where(cls.model.rooms_quantity > 0)
            result = await session.execute(query)
            return result.scalars().all()
        
