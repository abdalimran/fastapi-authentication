from fastapi import APIRouter, Depends

from authentication import get_current_user
from models import User
from services.text_manipulations import text_upper, text_lower, text_reverse

text_router = APIRouter()


@text_router.get("/text-upper")
async def protected_route(text: str, user: User = Depends(get_current_user)):
    return {"text-original": text, "text-upper": text_upper(text)}


@text_router.get("/text-lower")
async def protected_route(text: str, user: User = Depends(get_current_user)):
    return {"text-original": text, "text-lower": text_lower(text)}


@text_router.get("/text-reverse")
async def protected_route(text: str, user: User = Depends(get_current_user)):
    return {"text-original": text, "text-reversed": text_reverse(text)}
