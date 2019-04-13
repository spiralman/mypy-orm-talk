# We want to define a record type, sort of like an instance of an ORM
# Model, but not coupled to the DB.

from mypy_extensions import TypedDict


class Book(TypedDict):
    author: str
    title: str
