class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    class Library:
        def __init__(self):
            self.books = []

        def add_book(self, book):
            """Add a book to the library."""
            self.books.append(book)

        def remove_book(self, title):
            """Remove a book from the library by title."""
            self.books = [book for book in self.books if book.title != title]

        def list_books(self):
            """List all books in the library."""
            return [(book.title, book.author, book._is_checked_out) for book in self.books]

        def check_out_book(self, title):
            """Check out a book from the library by title."""
            for book in self.books:
                if book.title == title:
                    book._is_checked_out = True
                    return True
            return False
        def return_book(self, title):
            """Return a book to the library by title."""
            for book in self.books:
                if book.title == title:
                    book._is_checked_out = False
                    return True
            return False