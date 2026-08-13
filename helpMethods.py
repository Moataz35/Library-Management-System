from library import Library
from bookCategory import BookCategory
from accountManager import UserNotFound, DuplicateUsername, IncorrectPassword

def getNumber(prompt = "", numberType = float):
    while True:
        try:
            num = numberType(input(prompt))
        except ValueError as e:
            print("Invalid Input. It should be a number")
        else:
            break
    return num


def getNumberInRange(rangeStart, rangeEnd):
    prompt = f"Enter a number between {rangeStart} and {rangeEnd}: "
    num = getNumber(prompt, int)

    while not (num >= rangeStart and num <= rangeEnd):
        print("Invalid Number")
        num = getNumber(prompt, int)

    return num

def printAsMenu(anyList: list):

    for i in range(len(anyList)):
        print(f"{i + 1}. {anyList[i]}")

def getUsernameFromLoginScreen(libraryObject: Library):

    username = getNonEmptyInput("Username: ")
    password = getNonEmptyInput("Password: ")

    successful_login = False
    while not successful_login:
        try:
            libraryObject.accountManager.logIn(username, password)

        except UserNotFound:
            print("Invalid Username")
            username = getNonEmptyInput("Username: ")

        except IncorrectPassword:
            print("Incorrect Password")
            password = getNonEmptyInput("Password: ")

        else:
            successful_login = True

    return username

def getUsernameFromSignUpScreen(libraryObject: Library):

    firstName = getNonEmptyInput("First Name: ")
    lastName = getNonEmptyInput("Last Name: ")
    nationalID = getNonEmptyInput("National ID: ")
    username = getNonEmptyInput("Username: ")
    password = getNonEmptyInput("Password: ")

    successful_signUp = False
    while not successful_signUp:
        try:
            libraryObject.accountManager.signUp(firstName, lastName, nationalID, username, password)

        except DuplicateUsername:

            print("Username already exists. Try another one.")
            username = getNonEmptyInput("Username: ")

        else:
            successful_signUp = True

    return username

def getCategoryInput(prompt = "Enter a book category: ") -> BookCategory:
    category = None
    while True:
        try:
            BookCategory.printCategories()
            userInput = input(prompt)
            category = BookCategory.getCategory(userInput)
        except ValueError:
            print("Invalid Category Name")
        else:
            break

    return category

def getNonEmptyInput(prompt = ""):

    userInput = input(prompt)

    while (userInput is None) or (len(userInput) == 0) or userInput.isspace():
        print("You should enter a non empty string.")
        userInput = input(prompt)

    return userInput
