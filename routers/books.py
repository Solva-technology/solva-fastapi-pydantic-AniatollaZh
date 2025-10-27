from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, model_validator
from typing import List
from models.fake_db import books, authors

router = APIRouter(prefix="/books")

class Book(BaseModel):
    id: int | None = None
    title: str = Field(..., min_length=2)
    author_id: int
    year: int = Field(..., ge=1000, le=2100)

    @model_validator(mode="before")
    def validate_author(cls, values):
        author_id = values.get("author_id")
        if not any(a["id"] == author_id for a in authors):
            raise ValueError("Author ID does not exist")
        return values

@router.get("/", response_model=List[Book])
def get_books():
    return books

@router.post("/", response_model=Book)
def add_book(book: Book):
    book.id = max([b["id"] for b in books], default=0) + 1
    books.append(book.model_dump())
    return book

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
