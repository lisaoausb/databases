from lib.comment import *

"""
comment constructs with an id, name and starting_date
"""
def test_comment_constructs():
    comment = Comment(1, "Content", 'Author', 1)
    assert comment.id == 1
    assert comment.content == "Content"
    assert comment.author == 'Author'
    assert comment.post_id == 1

"""
We can format comment  s to strings nicely
"""
def test_comments_format_nicely():
    comment = Comment(1, "Content", 'Author', 1)
    assert str(comment ) == "Comment(1, Content, Author, 1)"
    # Try commenting out the `__repr__` method in lib/comment  .py
    # And see what happens when you run this test again.

"""
We can compare two identical comment   s
And have them be equal
"""
def test_comments_are_equal():
    comment1 = Comment(1, "Content", 'Author', 1)
    comment2 = Comment(1, "Content", 'Author', 1)
    assert comment1 == comment2
    # Try commenting out the `__eq__` method in lib/comment.py
    # And see what happens when you run this test again.
