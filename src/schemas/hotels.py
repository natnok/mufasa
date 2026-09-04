from pydantic import BaseModel, ConfigDict


class HotelsPost(BaseModel):
    title: str
    stars: str


class HotelsPatch(BaseModel):
    title: str | None = None
    stars: str | None = None


class HotelsData(HotelsPost):
    hotel_id: int

    model_config = ConfigDict(from_attributes=True)


class HotelsResponce(HotelsData):
    pass
