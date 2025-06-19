from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from api_v1.models.people_model import GendersModel, PeopleModel, ParentsModel
from api_v1.schemas.people_schema import PeopleSchema

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
    )
    session.add(insert_parents)
    await session.commit()
    return {
        "status": 200,
        "data": data
    }

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