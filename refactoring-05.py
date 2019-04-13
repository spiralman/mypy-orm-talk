# Now, we want to be able to use the book in series function from
# find_related. But, we have to do some checking, to ensure that the
# book passed in belongs to a series.

# Unfortunately, MyPy isn't quite smart enough to avoid the cast. But,
# non-the-less, we can at least trust that, once we've performed the
# check, the rest of the code can be guaranteed that the attribute is
# there.

# Also, note that MyPy is smart enough to know that a BookInSeries can
# be used where you expect a Book

from typing import Optional, cast
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


def find_related(book: Book) -> Optional[Book]:
    if "series" in book:
        return find_other_in_series(cast(BookInSeries, book))

    return None

def find_other_in_series(book: BookInSeries) -> Optional[BookInSeries]:
    row = db.find({"series": book["series"]})

    if row is not None:
        return parse_book_in_series(row)

    return None
