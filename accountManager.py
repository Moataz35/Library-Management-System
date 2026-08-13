from account import Account
import json
import hashlib

class AccountManager:
    def __init__(self, storageFileName = "accounts.json"):

        self.fileName = storageFileName
        self.accounts = {}
        self.getStoredAccounts()

    def logIn(self, username, password):

        userData = self.accounts.get(username)

        if userData == None:
            raise UserNotFound

        hashedPassword = AccountManager.getHashString(password)

        if hashedPassword != userData["Password"]:
            raise IncorrectPassword
        
        self.accounts[username]["Logged"] = True

    def logOut(self, username):

        userData = self.accounts.get(username)
        
        if userData == None:
            raise UserNotFound

        self.accounts[username]["Logged"] = False

    def signUp(self, firstName, lastName, nationalID, username, password):

        userData = self.accounts.get(username)
                
        if userData is not None:
            raise DuplicateUsername("There is already a user with this username.")

        hashedPassword = AccountManager.getHashString(password)

        newAccount = Account(
            firstName=firstName,
            lastName=lastName,
            nationalID=nationalID,
            username=username,
            password=hashedPassword
        )

        accountDict = newAccount.asDict()
        accountDict[username]["Logged"] = True

        self.accounts.update(accountDict)

    def isAdmin(self, username):

        userData = self.accounts.get(username)
                
        if userData == None:
            raise UserNotFound

        return str.casefold(userData["Role"]) == str.casefold("Admin")

    def isLogged(self, username):

        userData = self.accounts.get(username)
                        
        if userData == None:
            raise UserNotFound

        return userData["Logged"] == True

    def updateAccountDetails(self, username, newDetails):
        
        self.accounts.update({username:newDetails})

    def getStoredAccounts(self):
    
        with open(self.fileName) as f:
            self.accounts = json.load(f)

    def updateAccounts(self):
    
        with open(self.fileName, "w") as f:
            json.dump(self.accounts, f, indent=2)

    @staticmethod
    def getHashString(rawString: str):

        hashObject = hashlib.sha256(rawString.encode())
        hashedString = hashObject.hexdigest()
        return hashedString


class UserNotFound(Exception):
    pass

class IncorrectPassword(Exception):
    pass

class DuplicateUsername(Exception):
    pass
