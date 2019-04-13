# We need to be able to take a result from the database, or user
# input, and turn it into an instance of our "model"

from mypy_extensions import TypedDict


class Book(TypedDict):
    author: str
    title: str


def parse_book(request: dict) -> Book:
    return Book(author=request["author"], title=request["title"])
