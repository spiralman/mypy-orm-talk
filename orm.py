from typing import NamedTuple

import db


class Book(NamedTuple):
    author: str
    title: str


def parse_book(request: dict) -> Book:
    return Book(author=request["author"], title=request["title"])


def save_book(book: Book) -> None:
    db.insert({
        "author": book.author,
        "title": book.title
    })
