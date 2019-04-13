from mypy_extensions import TypedDict


class Book(TypedDict):
    author: str
    title: str
