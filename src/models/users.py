from pydantic import EmailStr
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class UsersORM(Base):
    __tablename__ = "users"

    users_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[EmailStr] = mapped_column(String(200))
    hashed_pawwsord: Mapped[str] = mapped_column()
