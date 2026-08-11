from library import Library
from book import Book
from helpMethods import getNumberInRange
from person import Person
from libraryExceptions import BookNotFound
from bookCategory import getCategoryInput

print("Welcome to my library")

print("Are you...?")
print("1. Admin")
print("2. Customer")

userChoice = getNumberInRange(1, 2)

myLibrary = Library()

print("What do you want to do?")
if userChoice == 1:

    adminMenu = [
        "Add a book",
        "Remove a book"
    ]

    for i in range(len(adminMenu)):
        print(f"{i + 1}. {adminMenu[i]}")

    adminChoice = getNumberInRange(1, len(adminMenu))

    if adminChoice == 1:

        bookTitle = input("Book Title: ")
        bookAuthor = input("Author: ")
        bookCategory = getCategoryInput("Category: ")
        myLibrary.addBook(bookTitle, bookAuthor, bookCategory)
        print("The book was added successfully.")
        
    else:

        bookTitle = input("Book Title: ")
        try:
            myLibrary.removeBook(bookTitle)
        except BookNotFound:
            print("This book doesn't exist.")

else:

    customerMenu = [
        "Borrow a book",
        "Return a book"
    ]

    for i in range(len(customerMenu)):
        print(f"{i + 1}. {customerMenu[i]}")

    customerChoice = getNumberInRange(1, len(customerMenu))

    if customerChoice == 1:

        bookTitle = input("Book Title: ")

        try:
            orderedBook = myLibrary.borrowBook(bookTitle)
        except BookNotFound:
            print(f"We don't have '{bookTitle}' book.")
        else:
            print("Successful borrowing operation.")

    else:
        bookTitle = input("Book Title: ")
        myLibrary.returnBook(bookTitle)
        print("Thank you for returning the book on time")


myLibrary.updateRepository()
