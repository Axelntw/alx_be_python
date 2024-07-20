# This file implements a simple library system with classes for Book, EBook, PrintBook, and Library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        result = f"{self.__class__.__name__}: {self.title} by {self.author}"
        if isinstance(self, EBook):
            result += f", File Size: {self.file_size}KB"
        elif isinstance(self, PrintBook):
            result += f", Page Count: {self.page_count}"
        return result
    
    def __repr__(self):
        result = f"{self.__class__.__name__}: {self.title} by {self.author}"
        if isinstance(self, EBook):
            result += f", File Size: {self.file_size}KB"
        elif isinstance(self, PrintBook):
            result += f", Page Count: {self.page_count}"
        return result
    
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
        [print(book) for book in self.books]