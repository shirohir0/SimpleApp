from .database_router import router as database_router
from .people_router import router as people_router

routes = [database_router, people_router]