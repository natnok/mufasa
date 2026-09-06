from pydantic import BaseModel


class HotelsPost(BaseModel):
    title: str
    stars: int


class HotelsPatch(BaseModel):
    title: str | None = None
    stars: int | None = None


class HotelsData(HotelsPost):
    hotel_id: int


class HotelsResponse(HotelsData):
    pass
