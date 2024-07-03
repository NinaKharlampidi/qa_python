from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()


        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_adding_three_books(self, collection):
        books = ['Гарри Поттер', 'Унесённые ветром', 'Дневник Бриджит Джонс']
        for book in books:
            collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 3

    @pytest.mark.parametrize('book',
                             ['', 'ОченьДлинноеНазваниеОченьДлинноеНазваниеОченьДлинноеНазвание']
                             )
    def test_add_new_book_add_incorrect_name_not_added(self, book, collection):
        collection.add_new_book(book)
        assert len(collection.get_books_genre()) == 0

    def test_set_book_genre_added(self, collection):
        first_book = 'Марсианские хроники'
        genre = 'Фантастика'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        assert collection.get_book_genre(first_book) == genre

    def test_set_book_genre_changed(self, collection):
        first_book = 'Марсианские хроники'
        genre = 'Фантастика'
        another_genre = 'Комедии'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, genre)
        collection.set_book_genre(first_book, another_genre)
        assert collection.get_book_genre(first_book) == another_genre

     def test_set_book_genre_nonexistent_genre_not_added(self, collection):
        first_book = 'Марсианские хроники'
        nonexistent_genre = 'Драмы'
        collection.add_new_book(first_book)
        collection.set_book_genre(first_book, nonexistent_genre)
        assert collection.get_book_genre(first_book) == ''


    def test_get_books_with_definite_genre_success(self, library):
        assert library.get_books_with_definite_genre('Детективы') == ['Шерлок Холмс']

    def test_get_books_for_children(self, library):
        for_children_books = library.get_books_for_children()
        assert for_children_books == ['Марсианские хроники', 'Малыш и Карлсон', 'Двенадцать стульев']


    def test_add_book_in_favorites_added(self, collection):
        first_book = 'Марсианские хроники'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        favorites = collection.get_list_of_favorites_books()
        assert len(favorites) == 1 and favorites[0] == first_book


    def test_delete_book_from_favorites_book_deleted(self, collection):
        first_book = 'Марсианские хроники'
        collection.add_new_book(first_book)
        collection.add_book_in_favorites(first_book)
        collection.delete_book_from_favorites(first_book)
        assert len(collection.get_list_of_favorites_books()) == 0