# routes/api.py
from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()
BASE_URL = "https://jsonplaceholder.typicode.com"

@router.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/users")
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Ошибка при получении users")
    return resp.json()

@router.get("/posts")
async def get_posts():
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{BASE_URL}/posts")
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Ошибка при получении posts")
    return resp.json()
