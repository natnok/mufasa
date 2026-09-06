from pydantic import BaseModel, ConfigDict, EmailStr


class UsersPostRequest(BaseModel):
    email: EmailStr
    password: str


class UsersPost(BaseModel):
    email: EmailStr
    hashed_password: str


class UsersPatch(BaseModel):
    email: EmailStr | None = None
    hashed_password: str | None = None


class UsersData(UsersPost):
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class UsersResponse(UsersData):
    pass
