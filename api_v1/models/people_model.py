from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class PeopleModel(Base):
    __tablename__ = 'peoples'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str]