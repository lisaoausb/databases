from lib.post_repository import *
from lib.post import *
from lib.comment import *

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blog.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    posts = repository.all() # Get all artists

    # Assert on the results
    assert posts == [
        Post(1, 'title1', 'content1'),
        Post(2, 'title2', 'content2'),
        Post(3, 'title3', 'content3')
    ]

"""
When we call PostRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    assert post == Post(1, "title1", "content1")

"""
When we call PostRepository#find_with_comments
we find a Post we indicate and get a list of all
the comments in this Post
"""

def test_get_single_post_and_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)

    post = repository.find_with_comments(1)
    assert post == Post(1, "title1", "content1", [Comment(2, 'comment2', 'author2', 1), Comment(6, "comment6", 'author4', 1)])


# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = ArtistRepository(db_connection)

#     repository.create(Artist(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(3, "Taylor Swift", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#         Artist(5, "The Beatles", "Rock"),
#     ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = ArtistRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#     ]
