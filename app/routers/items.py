from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import InventoryItem
from app.schemas import ItemCreate, ItemRead

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = InventoryItem(
        product=item.product,
        price=item.price,
        stock=item.stock,
        expiration_date=item.expiration_date,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
