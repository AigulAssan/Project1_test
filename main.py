from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal, engine, Base
import models

app = FastAPI()

# Создаём таблицы при старте
Base.metadata.create_all(bind=engine)

# Зависимость для подключения к БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "App connected successfully!"}
# Обновление от 15 октября