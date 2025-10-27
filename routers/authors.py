from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List
from models.fake_db import authors

router = APIRouter(prefix="/authors")

class Author(BaseModel):
    id: int | None = None
    name: str = Field(..., min_length=2)
    email: EmailStr

    @model_validator(mode="before")
    def check_name(cls, values):
        name = values.get("name")
        if name:
            values["name"] = name.title()
        return values

@router.get("/", response_model=List[Author])
def get_authors():
    return authors

@router.post("/", response_model=Author)
def add_author(author: Author):
    author.id = max([a["id"] for a in authors], default=0) + 1
    authors.append(author.model_dump())
    return author

@router.get("/{author_id}", response_model=Author)
def get_author(author_id: int):
    author = next((a for a in authors if a["id"] == author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author
