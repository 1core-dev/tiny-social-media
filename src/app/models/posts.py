from datetime import date

from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True
