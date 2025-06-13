from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime

class CarPostCreate(BaseModel):
    brand: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    year: int
    price: float = Field(..., gt=0)
    description: str = Field(..., min_length=1)
    is_active: Optional[bool] = True

class CarPostOut(BaseModel):
    id: int
    full_title: str
    price: float
    description: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
