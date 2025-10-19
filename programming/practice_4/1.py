from abc import ABC, abstractmethod
from datetime import datetime


class Printable(ABC):
    @abstractmethod
    def info(self) -> str: ...


class Product:
    category = "General"

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def description(self) -> str:
        return f"{self.name}: ${self.price:.2f} ({self.category})"


class Book(Product, Printable):
    category = "Books"

    def __init__(self, title: str, author: str, year: int, price: float):
        super().__init__(title, price)
        self.author = author
        self.year = year

    def info(self) -> str:
        return f"Title: {self.name}, Author: {self.author}, Year: {self.year}, Price: {self.price:.2f}"

    def __str__(self) -> str:
        return f"Title: {self.name}, Author: {self.author}, Year: {self.year}, Price: {self.price:.2f}"

    def __eq__(self, other) -> bool:
        return (
            self.name == other.name
            and self.year == other.year
            and self.price == other.price
        )

    @classmethod
    def from_string(cls, data):
        title, author, year, price = data.split(";")
        return cls(title, author, int(year), float(price))

    @property
    def age(self):
        return (datetime.now() - datetime(year=self.year, month=1, day=1)).days // 365


class Ebook(Book):
    category = "Ebooks"

    def __init__(
        self, title: str, author: str, year: int, price: float, file_format: str
    ):
        super().__init__(title, author, year, price)
        self.file_format = file_format

    def info(self) -> str:
        return f"Title: {self.name}, Author: {self.author}, Year: {self.year}, Price: {self.price:.2f}, Format: {self.file_format}"


gadget = Product("Smartphone", 699.99)
book = Book.from_string("1;2;1988;699.99")
ebook = Ebook("1", "2", 1488, 699.99, file_format="EPUB")
print(gadget.description())
print(book.info())
print(book.age)
print(ebook)
