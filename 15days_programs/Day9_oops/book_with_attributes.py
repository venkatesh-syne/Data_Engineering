class Book:

#__init__ → constructor (used to initialize values)
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Example usage
book1 = Book("Python Basics", "John Doe", 2022)

print(book1.display_info())