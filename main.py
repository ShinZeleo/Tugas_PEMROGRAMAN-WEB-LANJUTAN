from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET semua items
@app.get("/items/", response_model=list[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

# GET item berdasarkan ID
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item