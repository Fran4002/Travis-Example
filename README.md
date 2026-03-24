# Inventory Manager API

Simple FastAPI + SQLite project for inventory management.

## Implemented endpoint

- `POST /items/` - create a new inventory item

## Item fields

- `id`
- `product`
- `price`
- `stock`
- `expiration_date` (optional)

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Start server:
   - `uvicorn app.main:app --reload`

API docs are available at `/docs`.

## Tests

- Run:
  - `py.test -v`
