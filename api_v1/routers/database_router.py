from fastapi import APIRouter
from api_v1.database.engine import engine, new_session
from api_v1.models.people_model import Base
from api_v1.models.people_model import GendersModel

router = APIRouter(prefix='/api/v1/database', tags=['База данных'])

@router.post('/setup', 
          summary='Пересоздать базу данных',
        )
async def setup_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    async with new_session() as session:
        stmt = [GendersModel(gender="Мужской"), GendersModel(gender="Женский")]
        session.add_all(stmt)
        await session.commit()
    return {
        "status": 'OK',
        "code": 200,
        }

