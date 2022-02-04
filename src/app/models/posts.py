from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass
