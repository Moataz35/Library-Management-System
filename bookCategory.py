from enum import Enum, auto

class BookCategory(Enum):
    MYSTERY = auto()
    ROMANCE = auto()
    FANTASY = auto()
    SCIENCE = auto()

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def getCategory(categoryName: str):
        for category in BookCategory:
            if category.name.casefold() == categoryName.casefold():
                return category

        raise ValueError("Failed to convert to a BookCategory object")

    @staticmethod
    def isCategoryName(name: str):
        for category in BookCategory:
            if category.name.casefold() == name.casefold():
                return True

        return False

    @staticmethod
    def printCategories():
        print("Book Categories: [ ", end="")
        for category in BookCategory:
            print(category, end=" ")
        print("]")
######################################################################################

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
