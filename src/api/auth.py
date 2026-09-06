from fastapi import APIRouter, Response

from src.dependencies import DBDep
from src.schemas.response import ApiResponse
from src.schemas.users import UsersPostRequest, UsersResponse
from src.services.auth import AuthService

router = APIRouter()


@router.post("/register", response_model=ApiResponse[UsersResponse])
async def register_user(db: DBDep, data: UsersPostRequest):
    user = await AuthService(db).register_user(data=data)
    return ApiResponse(data=user)


@router.post("/login")
async def login_user(db: DBDep, data: UsersPostRequest, response: Response):
    access_token = await AuthService(db).login_user(data=data)
    response.set_cookie("access_token", access_token)


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
