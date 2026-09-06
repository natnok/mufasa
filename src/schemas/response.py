from pydantic import BaseModel


class ApiResponse[T](BaseModel):
    date: T
