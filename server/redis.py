from redis.asyncio import from_url
from redis.asyncio.client import Redis
from fastapi import WebSocketException

REDIS_URL = 'redis://localhost:6379'


async def get_pool():
    try:
        pool: Redis = await from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
        if pool is None:
            raise Exception()
        return pool
    except Exception:
        raise WebSocketException(code=1011, reason='internal error')
