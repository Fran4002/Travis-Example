from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_inventory.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_module():
    Base.metadata.create_all(bind=engine)


def teardown_module():
    Base.metadata.drop_all(bind=engine)


def test_create_item():
    payload = {
        "product": "Milk",
        "price": 2.50,
        "stock": 10,
        "expiration_date": "2026-12-31",
    }
    response = client.post("/items/", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["id"] > 0
    assert data["product"] == payload["product"]
    assert data["price"] == payload["price"]
    assert data["stock"] == payload["stock"]
    assert data["expiration_date"] == payload["expiration_date"]
