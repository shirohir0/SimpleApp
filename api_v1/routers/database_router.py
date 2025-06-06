from fastapi import APIRouter
from api_v1.database.engine import engine
from api_v1.models.people_model import Base

router = APIRouter(prefix='/api/v1/database', tags=['База данных'])

@router.post('/setup', 
          summary='Пересоздать базу данных',
        )
async def setup_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    return {
        "status": 'OK',
        "code": 200,
        }
