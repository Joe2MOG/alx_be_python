class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when a book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for end-user readability."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation to recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
