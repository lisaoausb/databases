from lib.post import *

"""
When I initialse,
Properties are set
"""

def test_initialises(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post = Post(1, 'title', 'content', 12, 1)
    assert post.id == 1
    assert post.title == 'title'
    assert post.content == 'content'
    assert post.number_of_views == 12
    assert post.user_id == 1

"""
When I have two instance with the same content, 
Python treats them as equal
"""

def test_equaliser(db_connection):
    post = Post(1, 'title', 'content', 12, 2)
    post1 = Post(1, 'title', 'content', 12, 2)
    assert post == post1

"""
custom formatting of my instances
"""

def test_format(db_connection):
    post = Post(1, 'title', 'content', 12, 2)
    assert str(post) == 'Post Nr 1: Title. Content by user 2. Views: 12'
