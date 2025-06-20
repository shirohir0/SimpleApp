# SimpleApp

A minimal FastAPI project for managing people and gender data. The service exposes a few API endpoints grouped under `/api/v1` and uses SQLAlchemy for database access.

## Setup

1. **Python**: Install Python 3.12 or newer.
2. **Create a virtual environment** (optional but recommended).
3. **Install dependencies**:

```bash
pip install "fastapi>=0.115.12,<0.116.0" \
            "uvicorn[standart]>=0.34.3,<0.35.0" \
            "sqlalchemy>=2.0.41,<3.0.0"
# Development dependencies
pip install "pytest==8.4.0"
```

These versions are taken from [`pyproject.toml`](pyproject.toml).

## Database configuration

The application expects database settings in `configs/postgres_config.py`. Create this file and provide a connection string for an async PostgreSQL database:

```python
# configs/postgres_config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    asyncpg_URL: str = "postgresql+asyncpg://user:password@localhost:5432/simpleapp"

settings = Settings()
```

`api_v1/database/engine.py` uses this configuration when creating the SQLAlchemy engine. A commented example for SQLite exists in that file if you prefer a local database.

After configuring the database, you can initialize it by sending a `POST` request to `/api/v1/database/setup` once the application is running.

## Running the application

From the repository root run:

```bash
uvicorn main:app --reload
```

The FastAPI server will start on `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` to explore the API documentation.

