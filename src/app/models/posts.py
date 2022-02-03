from datetime import date

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    created_at: date
    updated_at: date


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass
