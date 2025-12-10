from pydantic import BaseModel

class CreateBookSchema(BaseModel):
    """Scheme for creating a new book (validation of input data)."""
    title: str
    author: str
    year: int | None = None


class BookSchema(CreateBookSchema):
    """Schema for displaying a book (includes ID from the database)."""
    id: int


class BookUpdateSchema(BaseModel):
    """Scheme for updating a book."""
    title: str
    author: str
    year: int | None = None
