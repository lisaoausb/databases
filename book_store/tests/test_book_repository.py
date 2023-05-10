from lib.book_repository import *
from lib.book import *

"""
When we call BookRepository#all,
we get a list of all books in seed database.

this is where I pass the connection and call #seed (adding the path to the sql file)
"""

def test_all_returns_all_books(db_connection):
    db_connection.seed('seeds/book_store.sql')
    library = BookRepository(db_connection)
    books = library.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]

# books # => [book1, book2, book3, book4, book5]