# First, we try to define a function that can find another book in the
# same series. But, we also need to define a function for parsing a
# book that has a series attribute.

from typing import Optional
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


def parse_book_in_series(request: dict) -> BookInSeries:
    return BookInSeries(
        author=request["author"],
        title=request["title"],
        publisher=request["publisher"],
        series=request["series"])


def save_book(book: Book) -> None:
    db.insert({
        "author": book["author"],
        "title": book["title"],
        "publisher": book["publisher"]
    })


def find_related(book: Book) -> Book:
    pass

def find_other_in_series(book: BookInSeries) -> Optional[BookInSeries]:
    row = db.find({"series": book["series"]})

    if row is not None:
        return parse_book_in_series(row)

    return None
