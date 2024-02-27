from fastapi import FastAPI, Request, status, Depends
from fastapi.staticfiles import StaticFiles
from fastapi_users import fastapi_users, FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead

from src.operations.router import router as router_operation
from src.pages.router import router as router_pages
from src.chat.router import router as router_chat
# from src.tasks.router import router as router_tasks

# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.redis import RedisBackend

# import redis
# from redis import asyncio as aioredis


app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

app.include_router(router_operation)
app.include_router(router_pages)
app.include_router(router_chat)

# @app.on_event("startup")
# async def startup_event():
#     r = redis.Redis(host="localhost", port=6379, decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    