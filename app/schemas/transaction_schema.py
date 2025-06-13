from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    car_post_id: int
    buyer_id: int

class TransactionOut(BaseModel):
    id: int
    car_post_id: int
    buyer_id: int
    created_at: datetime

    class Config:
        orm_mode = True
