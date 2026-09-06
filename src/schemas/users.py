from pydantic import BaseModel


class UsersPost(BaseModel):
    email: str
    hashed_pawwsord: str


class UsersPatch(BaseModel):
    email: str | None = None
    hashed_pawwsord: str | None = None


class UsersData(UsersPost):
    users_id: int


class UsersResponse(UsersData):
    pass
