# main.py
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI(title="JSONPlaceholder proxy API")

# подключаем router с префиксом (если хочешь без префикса — убери prefix)
app.include_router(api_router)  # роуты будут на /users и /posts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

