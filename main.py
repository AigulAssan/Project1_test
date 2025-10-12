from fastapi import FastAPI
import httpx

app = FastAPI()

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.get("/users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users")
        return response.json()

@app.get("/posts")
async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts")
        return response.json()
