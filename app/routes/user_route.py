from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user_schema import UserCreate, UserOut
from app.services import user_service

router = APIRouter(prefix="/v1/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)
