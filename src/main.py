from fastapi import FastAPI, Request, status, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi_users import fastapi_users, FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead

from src.operations.router import router as router_operation
from src.pages.router import router as router_pages
from src.chat.router import router as router_chat


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

@app.get("/example")
def testing(user:UserRead = Depends(current_user)):
    if user.is_project_manager== True:
        return "yes"
    else: 
        raise HTTPException(status_code=403, detail="Доступ запрещен")