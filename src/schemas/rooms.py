from pydantic import BaseModel


class RoomsPost(BaseModel):
    number: int
    description: str


class RoomsPatch(BaseModel):
    number: int | None = None
    description: str | None = None


class RoomsData(RoomsPost):
    room_id: int


class RoomsResponse(RoomsData):
    pass
