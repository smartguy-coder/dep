from pydantic import BaseModel, Field, validator
from datetime import date


class Genre(BaseModel):
    name: str = Field(alias='genreTitleData')


class Book(BaseModel):
    title: str = Field(..., max_length=80)
    writer: str
    duration_sec: float = Field(..., gt=0)
    date: date
    summary: str
    genres: list[Genre] = None
    pages: int
