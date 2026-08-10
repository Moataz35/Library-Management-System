from enum import Enum, auto

class BookCategory(Enum):
    MYSTERY = auto()
    ROMANCE = auto()
    FANTASY = auto()
    SCIENCE = auto()

    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def getCategory(categoryName):
        for category in BookCategory:
            if category.name == categoryName:
                return category

        raise ValueError("Failed to convert to a BookCategory object")
