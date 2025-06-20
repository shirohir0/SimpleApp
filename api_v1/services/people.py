from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from api_v1.models.people_model import GendersModel, PeopleModel, ParentsModel
from api_v1.schemas.people_schema import PeopleSchema

async def get_all(session: AsyncSession):
    stmt = (
        select(PeopleModel)
        .options(joinedload(PeopleModel.gender))
        .options(
            selectinload(PeopleModel.parents)
            .joinedload(ParentsModel.mother)
            .joinedload(PeopleModel.gender)
        )
        .options(
            selectinload(PeopleModel.parents)
            .joinedload(ParentsModel.father)
            .joinedload(PeopleModel.gender)
        )
    )
    result = await session.execute(stmt)
    person = result.scalars().all()
    if person:
        return person
    return HTTPException(status_code=404, detail="Users not found")

async def get_people(id: int, session: AsyncSession):
    stmt = (
        select(PeopleModel)
        .options(joinedload(PeopleModel.gender))
        .options(
                selectinload(PeopleModel.parents)
                .joinedload(ParentsModel.mother)
                .joinedload(PeopleModel.gender)
            )
        .options(selectinload(PeopleModel.parents)
                .joinedload(ParentsModel.father)
                .joinedload(PeopleModel.gender)
            )
        .where(PeopleModel.id == id)
            )
    result = await session.execute(stmt)
    result = result.scalars().first()
    if result:
        data = {
            "statue": 200,
            "result": result
        }
        return data
    return HTTPException(status_code=404, detail="User not found")

async def create_people(data: PeopleSchema, session: AsyncSession):
    stmt = select(GendersModel).where(GendersModel.gender==data.gender)
    result = await session.execute(stmt)
    select_gender_id = result.scalars().first().id

    insert_people = PeopleModel(
        name = data.name,
        age = data.age,
        email = data.email,
        gender_id = select_gender_id
    )

    session.add(insert_people)
    await session.flush()

    insert_parents = ParentsModel(
        user_id = insert_people.id if data.mother or data.father else None,
        mother_id = data.mother if data.mother else None,
        father_id = data.father if data.father else None
    ) if data.mother or data.father else None
    session.add(insert_parents) if insert_parents else None
    await session.commit()
    return {
        "status": 200,
        "data": data
    }

async def put_people(id: int, data: PeopleSchema, session: AsyncSession):
    stmt = (
        select(PeopleModel)
        .options(joinedload(PeopleModel.gender))
        .options(
            selectinload(PeopleModel.parents)
            .selectinload(ParentsModel.mother)
            .joinedload(PeopleModel.gender)
        )
        .options(
            selectinload(PeopleModel.parents)
            .selectinload(ParentsModel.father)
            .joinedload(PeopleModel.gender)
        )
        .where(PeopleModel.id == id)
    )
    result = await session.execute(stmt)
    person = result.scalars().first()
    person.name = data.name
    person.age = data.age
    person.email = data.email
    person.gender_id = 1 if data.gender == 'Мужской' else 2 if data.gender == "Женский" else None

    if person.parents:
        person.parents.mother_id = data.mother if data.mother else None
        person.parents.father_id = data.father if data.father else None
    elif data.mother or data.father:
        print('asdadasdasd')
        session.add(ParentsModel(user_id=id, mother_id=data.mother, father_id=data.father))

    await session.commit()
    return {
        "update": data, 
        "status": 200
    }

async def delete_people(id: int, session: AsyncSession):
    stmt = (
        select(PeopleModel)
        .options(
            selectinload(PeopleModel.parents)
            .joinedload(ParentsModel.mother)
            .joinedload(PeopleModel.gender)
        )
        .options(
            selectinload(PeopleModel.parents)
            .joinedload(ParentsModel.father)
            .joinedload(PeopleModel.gender)
        )
        .where(PeopleModel.id==id)
    )
    result = await session.execute(stmt)
    data = result.scalars().first()
    to_return = {
        "id": data.id,
        "name": data.name,
        "age": data.age,
        "email": data.email,
        "gender": data.gender.gender,
        "parents":{
            "mother": {
                "name": data.parents.mother.name,
                "age": data.parents.mother.age,
                "email": data.parents.father.email
            },
            "father": {
                "name": data.parents.father.name,
                "age": data.parents.father.age,
                "email": data.parents.father.email
            }
        }
    }
    await session.delete(data)
    await session.commit()
    # await session.commit()
    return {
        "data": to_return,
        "status": 200,
        "message": f'User {to_return["name"]} deleted'
    }