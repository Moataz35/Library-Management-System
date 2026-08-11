from booksRepository import BooksRepository
from book import Book
from libraryExceptions import BookNotFound
from bookCategory import BookCategory

class Library:

    def __init__(self):

        self.availableBooks = BooksRepository("availableBooks.json")
        self.borrowedBooks = BooksRepository("borrowedBooks.json")

    def borrowBook(self, bookTitle) -> Book:

        if not self.isBookAvailable(bookTitle):
            raise BookNotFound(f"'{bookTitle}' is not available in the library.")

        book = self.availableBooks.removeBook(bookTitle)
        self.borrowedBooks.addBook(book)
        return book

    def returnBook(self, bookTitle):

        if self.isBookBorrowed(bookTitle):
            book = self.borrowedBooks.removeBook(bookTitle)
            self.availableBooks.addBook(book)

    def addBook(self, bookTitle, bookAuthor, bookCategory):

        if not BookCategory.isCategoryName(bookCategory):
            raise ValueError("Invalid Book Category.")

        book = Book(bookTitle, bookAuthor, bookCategory)
        self.availableBooks.addBook(book)

    def removeBook(self, bookTitle):

        book = self.availableBooks.removeBook(bookTitle)
        return book

    def isBookAvailable(self, bookTitle):
        return self.availableBooks.isInRepository(bookTitle)

    def isBookBorrowed(self, bookTitle):
        return self.borrowedBooks.isInRepository(bookTitle)

    def updateRepository(self):

        self.availableBooks.updateFile()
        self.borrowedBooks.updateFile()
