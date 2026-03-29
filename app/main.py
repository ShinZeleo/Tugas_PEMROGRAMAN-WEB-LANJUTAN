from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas
from app.db import engine, SessionLocal

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# =====================
# CONFIG
# =====================
SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# =====================
# DB
# =====================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =====================
# AUTH FUNCTION
# =====================
def hash_password(password: str):
    return pwd_context.hash(password[:72])

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user = db.query(models.User).filter(models.User.id == int(payload["sub"])).first()
    return user

# =====================
# AUTH ENDPOINT
# =====================
@app.post("/register")
def register(data: dict, db: Session = Depends(get_db)):
    user = models.User(
        email=data["email"],
        password=hash_password(data["password"]),
        role=data.get("role", "user")
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id}


@app.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data["email"]).first()

    if not user or not verify_password(data["password"], user.password):
        raise HTTPException(status_code=401)

    token = create_token({"sub": str(user.id), "role": user.role})
    return {"access_token": token}

# =====================
# CRUD ITEMS
# =====================
@app.post("/items/")
def create_item(item: schemas.ItemBase,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    new_item = models.Item(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.get("/items/")
def get_items(db: Session = Depends(get_db),
              user=Depends(get_current_user)):
    return db.query(models.Item).all()


@app.put("/items/{item_id}")
def update_item(item_id: int,
                item: schemas.ItemBase,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):
    data = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not data:
        raise HTTPException(status_code=404)

    data.name = item.name
    data.description = item.description
    db.commit()
    return data


@app.delete("/items/{item_id}")
def delete_item(item_id: int,
                db: Session = Depends(get_db),
                user=Depends(get_current_user)):

    if user.role != "admin":
        raise HTTPException(status_code=403)

    data = db.query(models.Item).filter(models.Item.id == item_id).first()

    if not data:
        raise HTTPException(status_code=404)

    db.delete(data)
    db.commit()
    return {"msg": "deleted"}