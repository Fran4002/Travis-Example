from fastapi import FastAPI

from app.database import Base, engine
from app.routers.items import router as items_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Manager API")
app.include_router(items_router)
