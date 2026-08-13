from library import Library
from libraryExceptions import BookNotFound
from helpMethods import *

print("Welcome to my library")
print("1. Login")
print("2. Sign up")

userChoice = getNumberInRange(1, 2)

myLibrary = Library()
username = None

if userChoice == 1:
    username = getUsernameFromLoginScreen(myLibrary)
else:
    username = getUsernameFromSignUpScreen(myLibrary)

userIsAdmin = myLibrary.accountManager.isAdmin(username)

print("What do you want to do?")
if userIsAdmin:

    adminMenu = [
        "Add a book",
        "Remove a book"
    ]

    printAsMenu(adminMenu)

    adminChoice = getNumberInRange(1, len(adminMenu))

    if adminChoice == 1:

        bookTitle = getNonEmptyInput("Book Title: ")
        bookAuthor = getNonEmptyInput("Author: ")
        bookCategory = getCategoryInput("Category: ")

        myLibrary.addBook(username, bookTitle, bookAuthor, bookCategory)
        print("The book was added successfully.")
        
    else:

        bookTitle = getNonEmptyInput("Book Title: ")
        try:
            myLibrary.removeBook(username, bookTitle)
        except BookNotFound:
            print("This book doesn't exist.")

else:

    customerMenu = [
        "Borrow a book",
        "Return a book"
    ]

    printAsMenu(customerMenu)

    customerChoice = getNumberInRange(1, len(customerMenu))

    if customerChoice == 1:

        bookTitle = getNonEmptyInput("Book Title: ")

        try:
            orderedBook = myLibrary.borrowBook(username, bookTitle)
        except BookNotFound as errorMessage:
            print(errorMessage)
        else:
            print("Successful borrowing operation.")

    else:

        bookTitle = getNonEmptyInput("Book Title: ")

        try:
            myLibrary.returnBook(username, bookTitle)
        except BookNotFound:
            print("You didn't borrow this book from us.")
        else:
            print("Thank you for returning the book on time")
            

myLibrary.accountManager.logOut(username)
myLibrary.updateStoredData()
