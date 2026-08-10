from library import Library
from book import Book
from helpMethods import getNumberInRange
from person import Person
from libraryExceptions import BookNotFound

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
        bookCategory = input("Category: ")

        newBook = Book(bookTitle, bookAuthor, bookCategory)
        myLibrary.addBook(newBook)
        print("The book was added successfully.")
        
    else:

        bookTitle = input("Book Title: ")
        try:
            myLibrary.removeBook(bookTitle)
        except BookNotFound as e:
            print(e)

else:

    customerMenu = [
        "Borrow a book",
        "Return a book"
    ]

    for i in range(len(customerMenu)):
        print(f"{i + 1}. {customerMenu[i]}")

    customerChoice = getNumberInRange(1, len(customerMenu))

    if customerChoice == 1:

        userName = input("Your name: ")
        userNationalID = input("Your national ID: ")
        userPhoneNumber = input("Your phone number: ")
        bookTitle = input("Book Title: ")

        customer = Person(userName, userNationalID, userPhoneNumber)
        try:
            orderedBook = myLibrary.borrowBook(customer, bookTitle)
        except BookNotFound as e:
            print(e)
        else:
            print(f"We don't have '{bookTitle}' book.")

    else:
        bookTitle = input("Book Title: ")
        myLibrary.returnBook(bookTitle)
        print("Thank you for returning the book on time")


myLibrary.updateRepository()
