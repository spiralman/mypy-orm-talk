# We want to save the "model" back out to the database. Note that the
# keys will always be present, and never null in the database.

from mypy_extensions import TypedDict
import db


class Book(TypedDict):
    author: str
    title: str


def parse_book(request: dict) -> Book:
    return Book(author=request["author"], title=request["title"])


def save_book(book: Book) -> None:
    db.insert({
        "author": book["author"],
        "title": book["title"]
    })
