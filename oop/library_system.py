# Base class - Book
class Book:
    def __init__(self, title, author):
        """Constructor to initialize title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for the Book class."""
        return f"Book: {self.title} by {self.author}"

# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor to initialize title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for the EBook class."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor to initialize title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for the PrintBook class."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class - Composition
class Library:
    def __init__(self):
        """Constructor to initialize the books collection."""
        self.books = []

    def add_book(self, book):
        """Method to add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Method to list all books in the library."""
        for book in self.books:
            print(book)
