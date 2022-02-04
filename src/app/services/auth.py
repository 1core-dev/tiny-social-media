from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.hash import bcrypt
from fastapi import HTTPException, status
from pydantic import ValidationError

from ..models.auth import User, Token
from .. import tables
from ..settings import settings


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hash_password: str) -> bool:
        return bcrypt.verify(plain_password, hash_password)

    @classmethod
    def hash_password(cls, plain_password: str):
        return bcrypt.hash(plain_password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exeption = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Couldn\'t validate credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=settings.jwt_algorithm
            )
        except JWTError:
            raise exeption

        user_data = payload.get('user')
        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exeption
        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)

        now = datetime.now()

        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expiration),
            'sub': str(user_data.id),
            'user': user_data.dict()
        }

        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm
        )
        return Token(access_token=token)
