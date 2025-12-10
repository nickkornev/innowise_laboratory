from fastapi import FastAPI
from app.api.v1.routers.books import router as books_router
from app.lifespan import lifespan


# Create the main instance of the FastAPI application
# lifespan=lifespan - pass the lifecycle manager to manage startup/stop
app = FastAPI(lifespan=lifespan)

# Connect the router to work with books
# All endpoints from books_router will become available in the application
app.include_router(books_router)

@app.get("/")
async def root():
    """Root endpoint for testing API operation."""
    return {"message": "Hello World"}