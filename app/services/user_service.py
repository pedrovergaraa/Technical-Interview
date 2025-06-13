from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserOut

def create_user(db: Session, user_data: UserCreate) -> UserOut:
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db: Session) -> list[UserOut]:
    return db.query(User).all()
