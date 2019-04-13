# Now we need to add a new required attribute to the model.

from mypy_extensions import TypedDict
import db


class Book(TypedDict):
    author: str
    title: str
    publisher: str


def parse_book(request: dict) -> Book:
    return Book(
        author=request["author"],
        title=request["title"],
        publisher=request["publisher"])


def save_book(book: Book) -> None:
    db.insert({
        "author": book["author"],
        "title": book["title"],
        "publisher": book["publisher"]
    })
