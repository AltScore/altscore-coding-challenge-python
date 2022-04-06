from fastapi import APIRouter
from server.api.endpoints.challenge import challenge_router

router = APIRouter()
router.include_router(
    router=challenge_router,
    prefix="/challenge"
)
