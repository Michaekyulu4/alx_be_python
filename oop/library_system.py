class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def  __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

    
class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(self,title,author, year)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return f"{super().__str__()} - EBook [{self.file_size_mb}MB]"
    
class PrintBook(Book):
    """Derived class for printed books."""
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} - PrintBook [{self.pages} pages]"

    
class Library:
    """Library class managing a collection of books."""
    def __init__(self):
        self.books = []  # Composition: Library has books

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)
        print(f"Added: {book}")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")

    

                     
