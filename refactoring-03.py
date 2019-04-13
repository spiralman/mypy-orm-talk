# We want to use this new type to add a feature to be able to find one
# book that's related to another book.

from mypy_extensions import TypedDict
import db


class Book(TypedDict):
    author: str
    title: str
    publisher: str


class BookInSeries(Book):
    series: str


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


def find_related(book: Book) -> Book:
    pass
