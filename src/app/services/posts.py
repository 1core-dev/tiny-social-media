from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.posts import PostCreate, PostUpdate


class PostsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, post_id: int) -> tables.Post:
        post = (
            self.session
                .query(tables.Post)
                .filter_by(id=post_id)
                .first()
        )
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get_posts(self) -> List[tables.Post]:
        posts = (
            self.session
                .query(tables.Post)
                .all()
        )
        return posts

    def get_post(self, post_id: int) -> tables.Post:
        return self._get(post_id)

    def create_post(self, post_data: PostCreate) -> tables.Post:
        post = tables.Post(**post_data.dict())
        self.session.add(post)
        self.session.commit()
        return post

    def update_post(self, post_id: int, post_data: PostUpdate) -> tables.Post:
        post = self._get(post_id)
        for field, value in post_data:
            setattr(post, field, value)
        self.session.commit()
        return post

    def delete_post(self, post_id: int) -> None:
        post = self._get(post_id)
        self.session.delete(post)
        self.session.commit()
