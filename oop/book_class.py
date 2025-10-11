class Book:
    """A class to represent a book."""

    def __init__(self, title, author, year):
        """Constructor: initializes title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation used for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: called when the object is deleted."""
        print(f"Deleting {self.title}")
