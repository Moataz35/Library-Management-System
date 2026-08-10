import json
from book import Book
from libraryExceptions import BookNotFound

class BooksRepository:
    def __init__(self, fileName):

        self.fileName = fileName
        self.booksList = []

        with open(fileName) as f:
            fileContent = json.load(f)
            dictList = list(fileContent)

            for dictionary in dictList:
                book = Book.fromDictionary(dictionary)
                self.booksList.append(book)

    def addBook(self, book: Book):
        
        if type(book) != Book:
            raise ValueError("Wrong data type for the book.")

        self.booksList.append(book)
        pass
    
    def removeBook(self, bookTitle):

        for book in self.booksList:
            if book.title == bookTitle:
                return book

        raise BookNotFound(f"'{bookTitle}' is not available in the repository.")

    def isInRepository(self, bookTitle):

        for book in self.booksList:
            if book.title == bookTitle:
                return True

        return False

    def updateFile(self):

        dictList = []
        for book in self.booksList:
            newDict = book.toDict()
            dictList.append(newDict)

        with open(self.fileName, "w") as f:
            json.dump(dictList, f, indent=2)
        
