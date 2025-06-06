from fastapi import APIRouter
from sqlalchemy import select
from api_v1.schemas.people_schema import PeopleSchema, PeopleSchemaID
from api_v1.database.engine import engine, session_depends
from api_v1.models.people_model import PeopleModel, Base
from api_v1.simple_utills.error_message import check_users

router = APIRouter(prefix='/peoples', tags=['Пользователи'])

@router.get(
        '/people', 
        summary='Получить всех пользователей',
        )
async def get_all_peoples(session: session_depends) -> list[PeopleSchemaID]:
    data = select(PeopleModel)
    result = await session.execute(data)
    all_results = result.scalars().all()
    await check_users(all_results)

    return all_results

@router.get(
        '/people/{id}',
        summary='Получить пользователя по id',
        )
async def get_people_by_id(id: int, session: session_depends):
    data = await session.get(PeopleModel, id)
    await check_users(data, id=id)

    return data

@router.post(
        '/people',
        summary='Добавить пользователя',
        )
async def add_people(data: PeopleSchema, session: session_depends):
    new_people = PeopleModel(
        name = data.name,
        age =  data.age,
        email = data.email
    )

    session.add(new_people)
    await session.commit()
    # await session.refresh(new_people)
    return {
        "data": {
            "id": new_people.id,
            "name": new_people.name,
            "age": new_people.age,
            "email": new_people.email
            },
        "status": 200
    }

@router.put(
        "/people",
        summary='Изменить пользователя',
        )
async def update_people(data: PeopleSchemaID, session: session_depends):
    user = await session.get(PeopleModel, data.id)
    await check_users(user, id=data.id)
    
    user.name = data.name
    user.email = data.email
    user.age = data.age
    await session.commit()
    return {
        "data": {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "email": user.email},
        "status": 200,
        "message": 'user was changed success'
    }

@router.delete("/people/{id}", 
            summary='Удалить пользователя',
        )
async def delete_people(id: int, session: session_depends):
    user = await session.get(PeopleModel, id)
    await check_users(user, id=id)

    name = user.name
    user_id = user.id
    await session.delete(user)
    await session.commit()
    return {
        "data": {
            "name": name,
            "id": user_id,
            "status": 200
            },
        "status": 200,
        "message": 'user was delete success'
    }