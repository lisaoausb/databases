from lib.book import *

class BookRepository():
    # Selecting all books
    # No arguments 
    def __init__(self, connection):
        # Initialise data base connection
        # Parameter: connection
        self._connection = connection

    def all(self):
        all_books = self._connection.execute('SELECT * FROM books;')
        books = []
        for book in all_books:
            book_instance = Book(book['id'], book['title'], book['author_name'])
            books.append(book_instance)

        return books
        # Executes the SQL query:
        # SELECT * FROM books;
        # executing the SQL query will give me all the rows in the table (every row is a dictionary, so need to extract what I want and add to a list)
        # need to use the extracted bits to populate model class instances 
        # Returns a LIST of Book objects