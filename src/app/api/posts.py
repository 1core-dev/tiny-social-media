from typing import List

from fastapi import APIRouter, Depends, Response, status

from ..models.posts import Post, PostCreate, PostUpdate
from ..services.posts import PostsService

router = APIRouter(prefix='/posts')


@router.get('/', response_model=List[Post])
def get_posts(service: PostsService = Depends()):
    return service.get_posts()


@router.post('/', response_model=Post)
def create_post(
        post_data: PostCreate,
        service: PostsService = Depends()
):
    return service.create_post(post_data)


@router.get('/{post_id}', response_model=Post)
def get_post(
        post_id: int,
        service: PostsService = Depends()
):
    return service.get_post(post_id)


@router.put('/{post_id}', response_model=Post)
def update_post(
        post_id: int,
        post_data: PostUpdate,
        service: PostsService = Depends()
):
    return service.update_post(post_id, post_data)


@router.delete('/{post_id}')
def delete_post(
        post_id: int,
        service: PostsService = Depends()
):
    service.delete_post(post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
