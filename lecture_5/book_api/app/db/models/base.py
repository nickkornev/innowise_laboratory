from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    The base class for all SQLAlchemy models.

    Inherits from DeclarativeBase, providing common configuration
    for all application models. Defines standard fields and behavior
    that will be inherited by all child models.

    Attributes:
    id (int): The default primary key for all models.
    Automatically added to every table.
    """
    id: Mapped[int] = mapped_column(primary_key=True)