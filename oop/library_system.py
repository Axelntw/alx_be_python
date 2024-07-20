# This file implements a simple library system with classes for Book, EBook, PrintBook, and Library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(f"{book.__class__.__name__}: {book.title} by {book.author}", end="")
            if isinstance(book, EBook):
                print(f", File Size: {book.file_size} KB")
            elif isinstance(book, PrintBook):
                print(f", Page Count: {book.page_count}")
            else:
                print()
