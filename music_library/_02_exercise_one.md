02_test_driving_model_repository_classes EXERCISE
Model and Repository Classes Design Recipe

1. Design and create the Table

If the table is already created in the database, you can skip this step.

2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

Table name: albums

Model class (in lib/album.py)
class Album

Repository class (in lib/album_repository.py)
class AlbumRepository

4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

Table name: albums
 
Model class
(in lib/album.py)

class Album
    def __init__(self, id, title, release_year, artist_id):
        self.id = 0
        self.title = ""
        self.release_year = 0
        self.artist_id = 0

5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

Table name: albums

Repository class
(in lib/album_repository.py)

class AlbumRepository
    # Selecting all records
    # No arguments 
    def __init__(self):
        pass

    def all(self):
        # Executes the SQL query:
        # SELECT * FROM albums;

        # Returns a list of Album objects

6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

"""
When we call AlbumRepository#all,
we get a list of all albums in seed database.
"""

library = AlbumRepository()

albums = library.all()

len(albums) # => 12

albums[0].id # => 1
albums[0].title # => 'Doolittle'
albums[0].release_year # => 1989
albums[0].artist_id # => 1

albums[8].id # => 9
albums[8].title # => 'Baltimore'
albums[8].release_year # => 1978
albums[8].artist_id # => 4

Encode this example as a test.

7. Test-drive and implement the Repository class behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.