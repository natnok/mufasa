from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def get_all():
    pass


@router.get("/{room_id}")
async def get_one_or_none():
    pass


@router.post("")
async def post():
    pass


@router.put("/{room_id}")
async def put():
    pass


@router.patch("/{room_id}")
async def patch():
    pass


@router.delete("/{room_id}")
async def delete():
    pass
