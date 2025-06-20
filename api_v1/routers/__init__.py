from .database_router import router as database_router
from .people_router import router as people_router
from .gender_router import router as gender_router

routes = [database_router, people_router, gender_router]