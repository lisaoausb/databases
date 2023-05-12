from lib.post_repository import *
from lib.post import *

"""
When I call PostRepository#all,
all records in database are returned
"""

def test_all(db_connection):
    posts = PostRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    all_posts = posts.all()
    assert all_posts == [
        Post(1, 'title', 'content', 30, 2),
        Post(2, 'titel', 'inhalt', 2, 2),
        Post(3, 'titre', 'contenue', 1038, 1),
    ]

def test_find_one(db_connection):
    posts = PostRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    one_post = posts.find(2)
    assert one_post == Post(2, 'titel', 'inhalt', 2, 2)

def test_create_new(db_connection):
    posts = PostRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    new_post = Post(None, 'título', 'contenido', 295, 3)
    assert posts.create(new_post) == None
    assert posts.all() == [
        Post(1, 'title', 'content', 30, 2),
        Post(2, 'titel', 'inhalt', 2, 2),
        Post(3, 'titre', 'contenue', 1038, 1),
        Post(4, 'título', 'contenido', 295, 3)
    ]

def test_delete_post(db_connection):
    posts = PostRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    assert posts.delete(1) == None
    assert posts.all() == [
        Post(2, 'titel', 'inhalt', 2, 2),
        Post(3, 'titre', 'contenue', 1038, 1),
    ]

def test_update_post(db_connection):
    posts = PostRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    one_post = posts.find(1)
    one_post.number_of_views = 15
    posts.update(one_post)
    assert posts.find(1) == Post(1, 'title', 'content', 15, 2)
