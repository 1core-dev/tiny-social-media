from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.posts import PostCreate, PostUpdate


class PostsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> tables.Post:
        post = (
            self.session
                .query(tables.Post)
                .filter_by(
                id=post_id,
                user_id=user_id
            )
                .first()
        )
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get_posts(self, user_id: int) -> List[tables.Post]:
        posts = (
            self.session
                .query(tables.Post)
                .filter_by(user_id=user_id)
                .all()
        )
        return posts

    def get_post(self, user_id: int, post_id: int) -> tables.Post:
        return self._get(user_id, post_id)

    def create_post(self, user_id: int, post_data: PostCreate) -> tables.Post:
        post = tables.Post(
            **post_data.dict(),
            user_id=user_id)
        self.session.add(post)
        self.session.commit()
        return post

    def update_post(self, user_id: int, post_id: int, post_data: PostUpdate) -> tables.Post:
        post = self._get(user_id, post_id)
        for field, value in post_data:
            setattr(post, field, value)
        self.session.commit()
        return post

    def delete_post(self, user_id: int, post_id: int) -> None:
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
