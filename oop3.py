class ReversedStr(str):

    # new class method does not use self for immutable types like strings
    def __new__(*args, **kwargs):
        revstr = str.__new__(*args, **kwargs)
        revstr = revstr[::-1]
        return revstr

import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Bookcase:
    def __init__(self, books=None):
        self.books = books
        
    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)
