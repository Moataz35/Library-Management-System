from booksRepository import BooksRepository
from book import Book
from libraryExceptions import BookNotFound, AccessDenied
from bookCategory import BookCategory
from accountManager import AccountManager

class Library:

    def __init__(self):

        self.availableBooks = BooksRepository("availableBooks.json")
        self.borrowedBooks = BooksRepository("borrowedBooks.json")
        self.accountManager = AccountManager()

    def borrowBook(self, username, bookTitle) -> Book:

        if not self.accountManager.isLogged(username):
            raise AccessDenied("This user is not logged in.")

        if self.isBookBorrowed(bookTitle):
            raise BookNotFound(f"'{bookTitle}' is borrowed at this moment.")

        if not self.isBookAvailable(bookTitle):
            raise BookNotFound(f"'{bookTitle}' is not available in the library.")

        book = self.availableBooks.removeBook(bookTitle)
        self.borrowedBooks.addBook(book)
        return book

    def returnBook(self, username, bookTitle):

        if not self.accountManager.isLogged(username):
            raise AccessDenied("This user is not logged in.")

        if self.isBookBorrowed(bookTitle):
            book = self.borrowedBooks.removeBook(bookTitle)
            self.availableBooks.addBook(book)
        else:
            raise BookNotFound("This book is not borrowed")

    def addBook(self, username, bookTitle, bookAuthor, bookCategory):

        if (not self.accountManager.isAdmin(username)) or (not self.accountManager.isLogged(username)):
            raise AccessDenied("Only admins are allowed to add books.")

        if (type(bookCategory) is str) and (not BookCategory.isCategoryName(bookCategory)):
            raise ValueError("Invalid Book Category.")

        if type(bookCategory) is str:
            bookCategory = BookCategory.getCategory(bookCategory)

        book = Book(bookTitle, bookAuthor, bookCategory)
        self.availableBooks.addBook(book)

    def removeBook(self, username, bookTitle):

        if (not self.accountManager.isAdmin(username)) or (not self.accountManager.isLogged(username)):
            raise AccessDenied("Only admins are allowed to remove books.")

        if not self.isBookAvailable:
            raise BookNotFound("This book is not available now.")

        book = self.availableBooks.removeBook(bookTitle)
        return book

    def isBookAvailable(self, bookTitle):
        return self.availableBooks.isInRepository(bookTitle)

    def isBookBorrowed(self, bookTitle):
        return self.borrowedBooks.isInRepository(bookTitle)

    def updateStoredData(self):

        self.availableBooks.updateFile()
        self.borrowedBooks.updateFile()
        self.accountManager.updateAccounts()
