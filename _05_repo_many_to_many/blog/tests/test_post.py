from lib.post import *

"""
post constructs with an id, name and starting_date
"""
def test_post_constructs():
    post = Post(1, "test title")
    assert post.id == 1
    assert post.title == "test title"

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "test title")
    assert str(post) == "Post(1, test title)"
    # Try commenting out the `__repr__` method in lib/post.py
    # And see what happens when you run this test again.

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "test title")
    post2 = Post(1, "test title")
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/post.py
    # And see what happens when you run this test again.
