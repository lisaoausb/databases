02_test_driving_model_repository_classes CHALLENGE
Model and Repository Classes Design Recipe

1. Design and create the Table

If the table is already created in the database, you can skip this step.

2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

Table name: books

Model class (in lib/book.py)
class Book

Repository class (in lib/book_repository.py)
class BookRepository

4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

Table name: books
 
Model class
(in lib/book.py)

class Book
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name

    def __eq__():
        pass
        # remember to return

    def __repr__():
        pass
        # remember to return

5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

Table name: books

Repository class
(in lib/book_repository.py)

class BookRepository
    # Selecting all books
    # No arguments 
    def __init__(self, connection):
        # Initialise data base connection
        # Parameter: connection
        pass

    def all(self):
        # Executes the SQL query:
        # SELECT * FROM books;
        # executing the SQL query will give me all the rows in the table (every row is a dictionary, so need to extract what I want and add to a list)
        # Returns a LIST of Book objects

6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

"""
When we call BookRepository#all,
we get a list of all books in seed database.

this is where I pass the connection and call #seed (adding the path to the sql file)
"""

library = BookRepository()

books = library.all()

books # => [book1, book2, book3, book4, book5]

--------------------------------------------------

"""
Book classes construct as they should
"""

book = Book(id, title, author_name)

book.id # => 1
book.title # => Nineteen Eighty-Four
book.author_name # => George Orwell

"""
Two identical books are equal
"""
book1 = Book(1, 'title', 'author')
book2 = Book(1, 'title', 'author')

# => book1 == book2 

"""
we format books as in the instructions
"""
book = Book()

book # => 1 - Nineteen Eighty-Four - George Orwell

7. Test-drive and implement the Repository class behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.