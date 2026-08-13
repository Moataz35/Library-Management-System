import hashlib

class Account:
    def __init__(self, firstName, lastName, nationalID, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.nationalID = nationalID
        self.username = username
        self.password = password
        self.role = "Customer"
        self.logged = False
        self.borrowedBooks = []

    def asDict(self):
        newDict = {
            self.username: {
                "First Name": self.firstName,
                "Last Name": self.lastName,
                "National ID": self.nationalID,
                "Password": self.password,
                "Role": self.role,
                "Logged": self.logged,
                "Borrowed Books": self.borrowedBooks
            }
        }
        return newDict
