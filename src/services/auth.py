from datetime import UTC, datetime, timedelta

import jwt
from pwdlib import PasswordHash

from src.config import settings
from src.schemas.users import UsersPost, UsersPostRequest
from src.services.base import BaseService


class AuthService(BaseService):
    password_hash = PasswordHash.recommended()

    def verify_password(self, plain_password, hashed_password):
        return self.password_hash.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.password_hash.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(UTC) + expires_delta
        else:
            expire = datetime.now(UTC) + timedelta(settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    async def register_user(self, data: UsersPostRequest):
        hashed_password = self.get_password_hash(data.password)
        new_data = UsersPost(email=data.email, hashed_password=hashed_password)
        user = await self.db.users.post(data=new_data)
        await self.db.commit()
        return user

    async def login_user(self, data: UsersPostRequest):
        user = await self.db.users.get_one_or_none(email=data.email)

        if user is None:
            raise ValueError("Некорректный email")

        if not self.verify_password(plain_password=data.password, hashed_password=user.hashed_password):  # type: ignore
            raise ValueError("Некорректный пароль")

        access_token = self.create_access_token({"user_id": user.user_id})  # type: ignore
        return access_token
