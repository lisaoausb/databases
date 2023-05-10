from lib.book import *

"""
Book classes construct as they should
"""

def test_constructs_as_inteded():
    book = Book(1, 'title', 'author')
    assert book.id == 1
    assert book.title == 'title'
    assert book.author_name == 'author'

"""
Two identical books are equal
"""

def test_same_is_equal():
    book1 = Book(1, 'title', 'author')
    book2 = Book(1, 'title', 'author')
    assert book1 == book2

"""
we format books as in the instructions
"""

def test_formatting():
    book1 = Book(1, 'title', 'author')
    assert str(book1) == '1 - title - author'