from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from app.db.models.base import Base


class Book(Base):
    """
    Book model in the database.

    Attributes:
    id (int): Unique book identifier (primary key)
    title (str): Book title (required)
    author (str): Book author (required)
    year (int | None): Publication year (optional)

    Table:
    Creates a 'book' table in the database with the following columns:
    - id: INTEGER PRIMARY KEY
    - title: VARCHAR NOT NULL
    - author: VARCHAR NOT NULL
    - year: INTEGER NULLABLE
    """
    __tablename__ = "book"
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=True)