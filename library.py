from booksRepository import BooksRepository
from book import Book
from libraryExceptions import BookNotFound

class Library:

    def __init__(self):

        self.availableBooks = BooksRepository("availableBooks.json")
        self.borrowedBooks = BooksRepository("borrowedBooks.json")

    def borrowBook(self, person, bookTitle) -> Book:

        if not self.isBookAvailable(bookTitle):
            raise BookNotFound(f"'{bookTitle}' is not available in the library.")

        book = self.availableBooks.removeBook(bookTitle)
        return book

    def returnBook(self, bookTitle):

        if self.isBookBorrowed(bookTitle):
            book = self.borrowedBooks.removeBook(bookTitle)
            self.availableBooks.addBook(book)

    def addBook(self, book):

        if type(book) != Book:
            raise ValueError("Wrong data type for the book.")

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
