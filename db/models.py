from datetime import datetime
from enum import Enum

from sqlalchemy import BigInteger, VARCHAR, Enum as alEnum, Column, DateTime, TEXT, DECIMAL, SMALLINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr, relationship


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):  # noqa
        return cls.__name__.lower() + 's'


class CreatedModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


class User(CreatedModel):
    class LangEnum(Enum):
        EN = "en"
        UZ = "uz"

    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    lang: Mapped[str] = mapped_column(alEnum(LangEnum,values_callable=lambda i: [field.value for field in i]),
                                      default=LangEnum.EN)
    phone_number: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return self.full_name


class Category(CreatedModel):
    __tablename__ = "categories" # noqa
    name: Mapped[str] = mapped_column(VARCHAR(255))
    books: Mapped[list['Book']] = relationship(back_populates="category")

    def __repr__(self):
        return self.name


class Book(CreatedModel):
    class VolType(Enum):
        HARD = 'hard'
        SOFT = 'soft'
    title: Mapped[str] = mapped_column(VARCHAR(255))
    description: Mapped[str] = mapped_column(TEXT, nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(precision=8, scale=2))
    page: Mapped[int]
    vol: Mapped[str]= mapped_column(alEnum(VolType, values_callable=lambda i: [field.value for field in i]),
                                    default=VolType.SOFT.value)
    quantity: Mapped[int] = mapped_column(SMALLINT, default=1)
    author: Mapped[str] = mapped_column(VARCHAR(255))
    photo_url: Mapped[str] = mapped_column(VARCHAR(255))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='CASCADE'))
    category: Mapped["Category"] = relationship(back_populates="books")

    def __repr__(self):
        return self.title
