from fastapi import APIRouter
from .posts import router as stats_router
from .auth import router as auth_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(stats_router)
