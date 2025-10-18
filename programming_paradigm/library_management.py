# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title            # public attribute
        self.author = author          # public attribute
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned/available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Already returned

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Book '{title}' checked out successfully.")
                    return True
                else:
                    print(f"Book '{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in library.")
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Book '{title}' returned successfully.")
                    return True
                else:
                    print(f"Book '{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in library.")
        return False

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        for book in available_books:
            print(book) 