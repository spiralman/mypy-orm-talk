from mypy_extensions import TypedDict


class Book(TypedDict):
    author: str
    title: str


def parse_book(request: dict) -> Book:
    return Book(author=request["author"], title=request["title"])
