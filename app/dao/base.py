from app.database import async_session_maker

from sqlalchemy import select, insert, delete


class DAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            bookings = await session.execute(query)
            return bookings.scalars().all()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()


    @classmethod 
    async def delete(cls, **data):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**data)
            await session.execute(query)
            await session.commit()

    
    @classmethod
    async def find_by_id_all(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(hotel_id=model_id)
            result = await session.execute(query)
            return result.scalars().all()

