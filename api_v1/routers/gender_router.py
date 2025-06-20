from fastapi import APIRouter
from api_v1.services import gender
from api_v1.database.engine import session_depends

router = APIRouter(prefix="/api/v1/gender", tags=['Пол'])

@router.delete(
        '/{id}',
        summary='Удалить пол'
)
async def delete_gender(id: int, session: session_depends):
    result = await gender.gender_delete(id, session)
    return result