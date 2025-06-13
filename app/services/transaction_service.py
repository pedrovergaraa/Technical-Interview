from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction_schema import TransactionCreate, TransactionOut

def create_transaction(db: Session, data: TransactionCreate) -> TransactionOut:
    transaction = Transaction(**data.dict())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_all_transactions(db: Session) -> list[TransactionOut]:
    return db.query(Transaction).all()
