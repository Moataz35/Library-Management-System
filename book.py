from bookCategory import BookCategory

class Book:
    def __init__(self, title: str, author: str, category: BookCategory):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nCategory: {self.category}"

    @staticmethod
    def fromDictionary(aDict: dict):
        
        bookTitle = aDict.get("Title")
        bookAuthor = aDict.get("Author")
        bookCategory = aDict.get("Category")

        if bookTitle is None or bookAuthor is None or bookCategory is None:
            raise ValueError("Invalid dictionary to convert to a book.")

        category = BookCategory.getCategory(bookCategory)

        return Book(bookTitle, bookAuthor, category)

    def asDict(self):
        asDict = {
            "Title": self.title,
            "Author": self.author,
            "Category": str(self.category)
        }
        return asDict
