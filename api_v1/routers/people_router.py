from fastapi import APIRouter
from api_v1.schemas.people_schema import PeopleSchema
from api_v1.database.engine import session_depends
from api_v1.services import people, gender

router = APIRouter(prefix='/api/v1/peoples', tags=['Пользователи'])

# @router.get(
#         '/', 
#         summary='Получить всех пользователей',
#         )
# async def get_all_peoples(session: session_depends) -> list[PeopleSchemaID]:
#     data = select(PeopleModel)
#     result = await session.execute(data)
#     all_results = result.scalars().all()
#     await check_users(all_results)

#     return all_results
@router.get(
        '/',
        summary='Получить всех пользователей'
)
async def get_all_people(session: session_depends):
    return await people.get_all(session)

@router.get(
    '/{id}',
    summary='Получить пользователя по ID'
)
async def get_people_by_id(id: int, session: session_depends):
    result = await people.get_people(id, session)

    return result

@router.post(
    '/',
    summary='Создать нового пользователя'
)
async def create_new_people(data: PeopleSchema, session: session_depends):
    result = await people.create_people(data, session)
    return result

@router.put(
    '/{id}',
    summary='Изменить все данные пользователя'
)
async def put_people_data(id: int, data: PeopleSchema, session: session_depends):
    result = await people.put_people(id, data, session)
    return result

@router.delete(
        '/{id}',
        summary='Удалить пользователя'
)
async def delet_people(id: int, session: session_depends):
    result = await people.delete_people(id, session)
    return result
