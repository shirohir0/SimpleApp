from fastapi import FastAPI
from api_v1.routers import routes
from api_v1.routers import database_router

app = FastAPI()
app.include_router(database_router)
for i in routes:
    app.include_router(i)