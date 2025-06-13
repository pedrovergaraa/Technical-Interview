from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.brand_schema import BrandCreate, BrandOut
from app.services import brand_service

router = APIRouter(prefix="/v1/brands", tags=["Brands"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BrandOut)
def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
    return brand_service.create_brand(db, brand)

@router.get("/", response_model=list[BrandOut])
def list_brands(db: Session = Depends(get_db)):
    return brand_service.get_all_brands(db)
