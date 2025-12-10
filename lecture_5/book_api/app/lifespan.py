from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.db_helper import db_helper
from app.db.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI application lifecycle context manager.
    Executed when the application starts and stops."""

    # create all tables in the database based on SQLAlchemy models
    async with db_helper.engine.begin() as conn:

        # run_sync allows to execute synchronous methods in an asynchronous context.
        # Base.metadata.create_all creates all tables defined in models.
        await conn.run_sync(Base.metadata.create_all)

    # The application is launched and ready to work
    yield