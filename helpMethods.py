from library import Library
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

    username = input("Username: ")
    password = input("Password: ")

    successful_login = False
    while not successful_login:
        try:
            libraryObject.accountManager.logIn(username, password)

        except UserNotFound:
            print("Invalid Username")
            username = input("Username: ")

        except IncorrectPassword:
            print("Incorrect Password")
            password = input("Password: ")

        else:
            successful_login = True

    return username

def getUsernameFromSignUpScreen(libraryObject: Library):

    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    nationalID = input("National ID: ")
    username = input("Username: ")
    password = input("Password: ")

    successful_signUp = False
    while not successful_signUp:
        try:
            libraryObject.accountManager.signUp(firstName, lastName, nationalID, username, password)

        except DuplicateUsername:

            print("Username already exists. Try another one.")
            username = input("Username: ")

        else:
            successful_signUp = True

    return username
