from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class PeopleModel(Base):
    __tablename__ = 'peoples'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str]
    gender_id: Mapped[int] = mapped_column(ForeignKey("people_genders.id", ondelete="SET NULL"), nullable=True)
    gender: Mapped["GendersModel"] = relationship("GendersModel", back_populates="peoples")
    parents: Mapped[Optional["ParentsModel"]] = relationship(
        "ParentsModel",
        back_populates="users",
        uselist=False,
        foreign_keys="[ParentsModel.user_id]",
        cascade="all, delete-orphan", # Очень важная штука для удаления столбцов с зависимостями

    )

class ParentsModel(Base):
    __tablename__ = 'people_parents'

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "peoples.id", 
            ondelete="CASCADE"
            ),
        primary_key=True
        )
    mother_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(
            "peoples.id",
            ondelete="SET NULL"
        )
    )
    father_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(
            "peoples.id",
            ondelete="SET NULL"
        )
    )

    users: Mapped["PeopleModel"] = relationship(
        "PeopleModel",
        back_populates="parents",
        foreign_keys=[user_id]
    )

    mother: Mapped["PeopleModel"] = relationship(
        "PeopleModel",
        foreign_keys=[mother_id],
    )

    father: Mapped["PeopleModel"] = relationship(
        "PeopleModel",
        foreign_keys=[father_id]
    )

class GendersModel(Base):
    __tablename__ = 'people_genders'

    id: Mapped[int] = mapped_column(primary_key=True)
    gender: Mapped[str]
    peoples: Mapped[List["PeopleModel"]] = relationship("PeopleModel", back_populates="gender")
