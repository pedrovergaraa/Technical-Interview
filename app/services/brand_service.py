from sqlalchemy.orm import Session
from app.models.brand import Brand
from app.schemas.brand_schema import BrandCreate, BrandOut

def create_brand(db: Session, brand_data: BrandCreate) -> BrandOut:
    brand = Brand(name=brand_data.name)
    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand

def get_all_brands(db: Session) -> list[BrandOut]:
    return db.query(Brand).all()
