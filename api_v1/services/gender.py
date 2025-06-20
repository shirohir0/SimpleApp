from api_v1.models.people_model import GendersModel
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

async def gender_delete(id: int, session: AsyncSession):
    stmt = await session.get(GendersModel, id)
    if stmt:
        result = {
            "id": stmt.id,
            "gender": stmt.gender,
        }
        await session.delete(stmt)

        await session.commit()
        
        return {
            "data": result,
            "status": 200,
            "message": "Gender deleted success"
        }
    return HTTPException(status_code=404, detail="Gender not found")