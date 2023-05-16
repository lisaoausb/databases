from lib.post_repository import *
from lib.post import *
from lib.tag import *

"""
When we call PostRepository#all
We get a list of Post ob jects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blog_posts_tags.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new ArtistRepository

    posts = repository.all() # Get all artists

    # Assert on the results
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
        ]

"""
When we call PostRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    assert post == Post(1,  "How to use Git")

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    posts = repository.find_by_tag('coding')
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics')]

def test_find_by_post(db_connection):
    db_connection.seed('seeds/blog_posts_tags.sql')
    repository = PostRepository(db_connection)
    posts = repository.find_by_post(3)
    assert posts == [Tag(1, 'coding'), Tag(4, 'education')]

# """
# When we call PostRepository#find_with_comments
# we find a Post we  indicate and get a list of all
# the comments in this Post
# """

# def test_get_single_post_and_comments(db_connection):
#     db_connection.seed("seeds/blog.sql")
#     repository = PostRepository(db_connection)

#     post = repository.find_with_comments(1)
#     assert post == Post(1,  "title1", "content1", [Comment(2, 'comment2', 'author2', 1), Comment(6, "comment6", 'author4', 1)])


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
