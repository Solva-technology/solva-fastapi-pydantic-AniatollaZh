from fastapi import FastAPI
from config import get_settings
from routers import authors, books

settings = get_settings()
app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(authors.router)
app.include_router(books.router)
