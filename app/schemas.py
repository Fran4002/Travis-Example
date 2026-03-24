from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ItemCreate(BaseModel):
    product: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)
    stock: int = Field(..., ge=0)
    expiration_date: Optional[date] = None


class ItemRead(BaseModel):
    id: int
    product: str
    price: float
    stock: int
    expiration_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)
