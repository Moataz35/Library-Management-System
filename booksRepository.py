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

        bookIndex = -1
        for i in range(len(self.booksList)):
            if self.booksList[i].title == bookTitle:
                bookIndex = i

        if bookIndex == -1:
            raise BookNotFound(f"'{bookTitle}' is not available in the repository.")

        book = self.booksList.pop(bookIndex)
        return book

    def isInRepository(self, bookTitle):

        for book in self.booksList:
            if book.title == bookTitle:
                return True

        return False

    def updateFile(self):

        dictList = []
        for book in self.booksList:
            newDict = book.asDict()
            dictList.append(newDict)

        with open(self.fileName, "w") as f:
            json.dump(dictList, f, indent=2)
        
