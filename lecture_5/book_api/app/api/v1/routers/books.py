from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db_helper import db_helper
from app.db.models import Book
from app.schemas.books import CreateBookSchema, BookSchema, BookUpdateSchema


router = APIRouter(prefix="/api/v1/books", tags=["books"])

@router.post("")
async def save_book(book_data: CreateBookSchema,
                    session: Annotated[AsyncSession, Depends(db_helper.get_session)]):
    """
    Creates a new book in the database.
    :param book_data: Data for creating a new book.
    :param session: Asynchronous database session.
    :return: The function does not return data, it only creates a record.
    """
    # Adding a new book to the session based on the passed data
    session.add(Book(**book_data.model_dump()))
    # Save changes to the database
    await session.commit()


@router.get("", response_model=list[BookSchema])
async def get_books(session: Annotated[AsyncSession, Depends(db_helper.get_session)]):
    """
    Gets a list of all books from the database.
    :param session: Asynchronous database session.
    :return: List of all books in BookSchema format.
    """
    # Create a query to select all books.
    query = select(Book)
    # Execute a query to the database.
    result = await session.execute(query)
    # Convert the result into a list of Book objects.
    return result.scalars().all()


@router.get("/{book_id}")
async def get_books(
    book_id: int,
    session: Annotated[AsyncSession, Depends(db_helper.get_session)]) -> BookSchema | None:
    """
    Get information about a specific book by its ID.
    :param book_id: Book ID.
    :param session: Asynchronous database session.
    :return: The book data or None if the book is not found.
    """
    # Create a query to search for a book by ID.
    query = select(Book).where(Book.id == book_id)
    # Execute the request.
    result = await session.execute(query)
    # Get one result or None.
    book = result.scalar_one_or_none()

    # If the book is not found, return a 404 error.
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    # Returning the found book.
    return book


@router.put("/{book_id}")
async def put_book(
        book_id: int,
        book_update: BookUpdateSchema,
        session: Annotated[AsyncSession, Depends(db_helper.get_session)]) -> BookSchema | None:
    """
    Updates information about a book by its ID.
    :param book_id: Book ID.
    :param book_update: Data for updating the book.
    :param session: Asynchronous database session.
    :return: Updated book details
    """
    # Create a query to search for a book by ID.
    query = select(Book).where(Book.id == book_id)
    # Execute the request.
    result = await session.execute(query)
    # Get one result or None.
    book = result.scalar_one_or_none()

    # If the book is not found, return a 404 error.
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    # Convert the update data into a dictionary, excluding undefined fields
    update_data = book_update.model_dump(exclude_unset=True)

    # Apply updates to the book object
    for field, value in update_data.items():
        setattr(book, field, value)

    # Save changes to the database.
    await session.commit()
    # Update the book object from the database.
    await session.refresh(book)

    # Return the updated book
    return book


@router.delete("/{book_id}")
async def delete_book(
        book_id: int,
        session: Annotated[AsyncSession, Depends(db_helper.get_session)]) -> BookSchema | None:
    """
    Deletes a book by its ID.
    :param book_id: Book ID.
    :param session: Asynchronous database session.
    :return: None: The function returns no data upon successful deletion.
    """
    # Create a query to search for a book by ID.
    query = select(Book).where(Book.id == book_id)
    # Execute the request.
    result = await session.execute(query)
    # Get one result or None.
    book = result.scalar_one_or_none()

    # If the book is not found, return a 404 error.
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    # Remove a book from a session
    await session.delete(book)
    # Delete a book
    await session.commit()

    # Return None
    return None
