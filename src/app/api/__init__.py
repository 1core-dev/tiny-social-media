from fastapi import APIRouter
from .posts import router as stats_router

router = APIRouter()
router.include_router(stats_router)
