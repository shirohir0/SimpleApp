from pydantic import BaseModel, Field, EmailStr, ConfigDict

class PeopleSchema(BaseModel):
    name: str = Field(max_length=80)
    age: int | None = Field(ge=0, le=1000)
    email: EmailStr

    model_config = ConfigDict(extra='forbid')

class PeopleSchemaID(PeopleSchema):
    id: int