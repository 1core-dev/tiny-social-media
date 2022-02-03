from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import tables
from ..models.posts import Post
from ..database import get_session

router = APIRouter(prefix='/posts')


@router.get('/', response_model=List[Post])
def get_post(session: Session = Depends(get_session)):
    posts = (
        session
        .query(tables.Post)
        .all()
    )
    return posts
