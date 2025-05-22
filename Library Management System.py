class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You have borrowed '{book.title}'.")
                return print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You have returned '{book.title}'.")
                return print(f"'{title}' was not borrowed or does not belong to this library.")


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("The Alchemist", "Paulo Coelho"))

library.show_books()

library.borrow_book("1984")
library.borrow_book("1984") 
library.return_book("1984")
library.return_book("1984")

print("\nUpdated Book List:")
library.show_books()
