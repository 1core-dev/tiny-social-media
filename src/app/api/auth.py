from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.auth import UserCreate, Token

router = APIRouter(
    prefix='/auth'
)


@router.post('/sign-up', response_model=Token)
def sign_up(user_data: UserCreate):
    pass


@router.get('/sign-in')
def sign_in(form_data: OAuth2PasswordRequestForm = Depends()):
    pass
