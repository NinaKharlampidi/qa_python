import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection


@pytest.fixture
def library(collection):
    collect = collection
    books = ['Марсианские хроники', 'Сияние', 'Шерлок Холмс', 'Малыш и Карлсон', 'Двенадцать стульев']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(5):
        collect.add_new_book(books[i])

    for i in range(5):
        collect.set_book_genre(books[i], genre[i])

    return collect