from fastapi import FastAPI

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_rooms

from app.pages.router import router as router_pages

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

app = FastAPI()

app.include_router(router_users)
app.include_router(router_hotels)
app.include_router(router_bookings)
app.include_router(router_rooms)
app.include_router(router_pages)



@app.on_event("startup")
async def startup():
    redis = await aioredis.create_redis_pool("redis://localhost:6379", encoding="utf8")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")