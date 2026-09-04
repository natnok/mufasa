from pydantic import BaseModel, ConfigDict


class RoomsPost(BaseModel):
    number: int
    description: str


class RoomsPatch(BaseModel):
    number: int | None = None
    description: str | None = None


class RoomsData(RoomsPost):
    room_id: int

    model_config = ConfigDict(from_attributes=True)


class RoomsResponce(RoomsData):
    pass
