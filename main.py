from fastapi import FastAPI
from api_v1.routers import routes

app = FastAPI()

for i in routes:
    app.include_router(i)