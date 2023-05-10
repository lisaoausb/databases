from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
#connection.seed("seeds/book_store.sql")

# Retrieve all artists
library = BookRepository(connection)
books = library.all()

# List them out
for book in books:
    print(book)
