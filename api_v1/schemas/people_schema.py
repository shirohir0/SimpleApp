from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ConfigDict

from pydantic import BaseModel, Field, EmailStr, ConfigDict

class PeopleSchema(BaseModel):
    name: str = Field(
        max_length=80,
        description="Полное имя пользователя (макс. 80 символов)",
        example="Имя Фамилия",
    )
    age: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Возраст (от 0 до 100). Необязательное поле.",
        example=35,
    )
    email: EmailStr = Field(
        description="Действующий email-адрес",
        example="mail@example.com",
    )

    gender: str = Field(
        max_length=20,
        description="Пол",
        example="Мужской"
    )

    mother: Optional[int] | None = Field(
        default=None,
        description="ID Матери",
        example=0,
    )

    father: Optional[int] | None = Field(
        default=None,
        description="ID Отца",
        example=0,
    )

    # model_config = ConfigDict(
    #     extra='forbid',
    #     json_schema_extra={
    #         "description": "Данные пользователя для регистрации или обновления",
    #         "examples": [{
    #             "name": "Имя Фамилия",
    #             "age": 40,
    #             "email": "mail@example.com",
    #         }],
    #     }
    # )

class PeopleSchemaID(PeopleSchema):
    id: int