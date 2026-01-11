from collections.abc import Iterator, Iterable
from typing import List, Any


# Конкретная коллекция
class BookCollection(Iterable):
    def __init__(self):
        self._books: List[str] = []

    def add_book(self, book: str):
        self._books.append(book)

    def __iter__(self) -> Iterator:
        return AlphabeticalIterator(self._books)


# Итератор по алфавиту
class AlphabeticalIterator(Iterator):
    def __init__(self, collection: List[str]):
        self._collection = sorted(collection)
        self._position = 0

    def __next__(self) -> str:
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()


# Итератор в обратном порядке
class ReverseIterator(Iterator):
    def __init__(self, collection: List[str]):
        self._collection = sorted(collection, reverse=True)
        self._position = 0

    def __next__(self) -> str:
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()


# Демонстрация
if __name__ == "__main__":
    library = BookCollection()
    library.add_book("Design Patterns")
    library.add_book("Clean Code")
    library.add_book("The Pragmatic Programmer")
    library.add_book("Refactoring")
    library.add_book("Introduction to Algorithms")

    print("=== Books in alphabetical order ===")
    for book in library:
        print(f"- {book}")

    print("\n=== Books in reverse alphabetical order ===")
    reverse_iter = ReverseIterator([book for book in library])
    for book in reverse_iter:
        print(f"- {book}")