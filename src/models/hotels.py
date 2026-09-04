from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class HotelsORM(Base):
    __tablename__ = "hotels"

    hotel_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    stars: Mapped[int] = mapped_column()
