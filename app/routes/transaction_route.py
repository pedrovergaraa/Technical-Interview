from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.transaction_schema import TransactionCreate, TransactionOut
from app.services import transaction_service

router = APIRouter(prefix="/v1/transactions", tags=["Transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TransactionOut)
def create_transaction(txn: TransactionCreate, db: Session = Depends(get_db)):
    return transaction_service.create_transaction(db, txn)

@router.get("/", response_model=list[TransactionOut])
def list_transactions(db: Session = Depends(get_db)):
    return transaction_service.get_all_transactions(db)
