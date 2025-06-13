from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.car_post_schema import CarPostCreate, CarPostOut
from app.services import car_post_service

router = APIRouter(prefix="/v1/cars", tags=["Cars Listing"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CarPostOut, status_code=status.HTTP_201_CREATED)
def create(post: CarPostCreate, db: Session = Depends(get_db)):
    return car_post_service.create_post(db, post)

@router.get("/", response_model=list[CarPostOut])
def list_all(db: Session = Depends(get_db)):
    return car_post_service.get_all_posts(db)

@router.get("/{post_id}", response_model=CarPostOut)
def get_one(post_id: int, db: Session = Depends(get_db)):
    post = car_post_service.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(404, "Post not found")
    
@router.get("/", response_model=list[CarPostOut])
def list_all(
    brand: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db)
):
    return car_post_service.get_filtered_posts(db, brand, year)


@router.put("/{post_id}", response_model=CarPostOut)
def update(post_id: int, post: CarPostCreate, db: Session = Depends(get_db)):
    updated = car_post_service.update_post(db, post_id, post)
    if not updated:
        raise HTTPException(404, "Post not found")
    return updated

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(post_id: int, db: Session = Depends(get_db)):
    if not car_post_service.delete_post(db, post_id):
        raise HTTPException(404, "Post not found")
