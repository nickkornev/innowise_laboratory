from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession


class DataBaseHelper:
    """Assistant for working with an asynchronous database via SQLAlchemy."""
    def __init__(self, url: str, echo: bool = False) -> None:
        # Create a database engine and session factory.
        self.engine = create_async_engine(url=url, echo=echo)
        self._session_factory = async_sessionmaker(bind=self.engine)

    async def get_session(self):
        """Generator for obtaining a DB session."""
        async with self._session_factory() as session:
            yield session

# Global instance for use throughout the application.
# Use SQLite with the asynchronous aiosqlite driver.
db_helper = DataBaseHelper(url="sqlite+aiosqlite:///db.sqlite3")