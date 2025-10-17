from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import db
from models import user as models
from schemas import user_schema as schemas
import httpx

app = FastAPI()

def get_db():
    database = db.SessionLocal()
    try:
        yield database
    finally:
        database.close()


@app.get("/users/", response_model=list[schemas.UserResponse])
def get_and_store_users(db: Session = Depends(get_db)):
    # 1️⃣ Пример получения данных с внешнего API
    response = httpx.get("https://jsonplaceholder.typicode.com/users")
    users_data = response.json()

    # 2️⃣ Сохраняем пользователей в БД, если их ещё нет
    for user_data in users_data:
        existing_user = db.query(models.User).filter(models.User.email == user_data["email"]).first()
        if not existing_user:
            db_user = models.User(name=user_data["name"], email=user_data["email"])
            db.add(db_user)
            db.commit()
            db.refresh(db_user)

    # 3️⃣ Возвращаем всех пользователей из БД
    return db.query(models.User).all()
