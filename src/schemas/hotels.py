from pydantic import BaseModel, ConfigDict


class HotelsPost(BaseModel):
    title: str
    stars: int


class HotelsPatch(BaseModel):
    title: str | None = None
    stars: int | None = None


class HotelsData(HotelsPost):
    hotel_id: int

    model_config = ConfigDict(from_attributes=True)


class HotelsResponse(HotelsData):
    pass
