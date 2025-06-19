from fastapi import APIRouter
from api_v1.schemas.people_schema import PeopleSchema, PeopleSchemaID
from api_v1.database.engine import session_depends
from api_v1.service.people import create_people, get_people

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

@router.post(
    '/',
    summary='Создать нового пользователя'
)
async def create_new_people(data: PeopleSchema, session: session_depends):
    result = await create_people(data, session)
    return result

@router.get(
    '/{id}',
    summary='Получить пользователя по ID'
)
async def get_people_by_id(id: int, session: session_depends):
    result = await get_people(id, session)

    return result



# @router.get(
#         '/{peopl_id}',
#         summary='Получить пользователя по id',
#         )
# async def get_people_by_id(people_id: int, session: session_depends):
#     data = await session.get(PeopleModel, people_id)
#     await check_users(data, id=people_id)

#     return data

# @router.post(
#         '/',
#         summary='Добавить пользователя',
#         )
# async def add_people(data: PeopleSchema, session: session_depends):
#     session.flush()
#     new_people = PeopleModel(
#         name = data.name,
#         age =  data.age,
#         email = data.email,
#         gender = data.gender
#     )

#     session.add(new_people)
#     await session.commit()
#     # await session.refresh(new_people)
#     return {
#         "data": {
#             "id": new_people.id,
#             "name": new_people.name,
#             "age": new_people.age,
#             "email": new_people.email
#             },
#         "status": 'OK',
#         "code": 200,
#     }

# @router.put(
#         "/{people_id}",
#         summary='Изменить пользователя',
#         )
# async def update_people(people_id: int, data: PeopleSchema, session: session_depends):
#     user = await session.get(PeopleModel, people_id)
#     await check_users(user, id=people_id)
    
#     user.name = data.name
#     user.email = data.email
#     user.age = data.age
#     await session.commit()
#     return {
#         "data": {
#             "id": user.id,
#             "name": user.name,
#             "age": user.age,
#             "email": user.email},
#         "status": 'OK',
#         "code": 200,
#         "message": 'user was changed success'
#     }

# @router.delete("/{people_id}", 
#             summary='Удалить пользователя',
#         )
# async def delete_people(people_id: int, session: session_depends):
#     user = await session.get(PeopleModel, people_id)
#     await check_users(user, id=people_id)

#     name = user.name
#     user_id = user.id
#     await session.delete(user)
#     await session.commit()
#     return {
#         "data": {
#             "name": name,
#             "id": user_id,
#             },
#         "status": 'OK',
#         "code": 200,
#         "message": 'user was delete success'
#     }

# @router.patch('/rename/{people_id}',
#               summary="Переименовать пользователя"
#               )
# async def rename_people(people_id: int, people_name: str, session: session_depends):
#     user = await session.get(PeopleModel, people_id)
#     await check_users(user, id)
#     user.name = people_name
#     await session.commit()
#     return {
#         "status": 'OK',
#         "code": 200,
#         "data":{
#             "user_id": user.id,
#             "new_name": user.name
#         }
#     }