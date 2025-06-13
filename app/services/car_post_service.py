from sqlalchemy.orm import Session
from app.models.car_post import CarPost
from app.schemas.car_post_schema import CarPostCreate, CarPostOut

def transform(post: CarPost) -> CarPostOut:
    return CarPostOut(
        id=post.id,
        full_title=f"{post.brand} {post.model} {post.year}",
        price=post.price,
        description=post.description,
        is_active=post.is_active,
        created_at=post.created_at
    )


def create_post(db: Session, post_data: CarPostCreate) -> CarPostOut:
    post = CarPost(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return transform(post)

def get_all_posts(db: Session) -> list[CarPostOut]:
    return [transform(p) for p in db.query(CarPost).all()]

def get_post_by_id(db: Session, post_id: int) -> CarPostOut | None:
    post = db.query(CarPost).filter(CarPost.id == post_id).first()
    return transform(post) if post else None

def get_filtered_posts(db: Session, brand: str | None, year: int | None) -> list[CarPostOut]:
    query = db.query(CarPost)
    if brand:
        query = query.filter(CarPost.brand.ilike(f"%{brand}%"))
    if year:
        query = query.filter(CarPost.year == year)
    return [transform(p) for p in query.all()]


def update_post(db: Session, post_id: int, post_data: CarPostCreate) -> CarPostOut | None:
    post = db.query(CarPost).filter(CarPost.id == post_id).first()
    if not post:
        return None
    for attr, value in post_data.dict().items():
        setattr(post, attr, value)
    db.commit()
    db.refresh(post)
    return transform(post)

def delete_post(db: Session, post_id: int) -> bool:
    post = db.query(CarPost).filter(CarPost.id == post_id).first()
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True
