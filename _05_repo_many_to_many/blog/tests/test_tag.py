from lib.tag import *

"""
tag constructs with an id, name and starting_date
"""
def test_tag_constructs():
    tag = Tag(1, "name")
    assert tag.id == 1
    assert tag.name == "name"

"""
We can format tags to strings nicely
"""
def test_tags_format_nicely():
    tag = Tag(1, "Content")
    assert str(tag) == "Tag(1, Content)"
    # Try taging out the `__repr__` method in lib/tag  .py
    # And see what happens when you run this test again.

"""
We can compare two identical tag   s
And have them be equal
"""
def test_tags_are_equal():
    tag1 = Tag(1, "Content")
    tag2 = Tag(1, "Content")
    assert tag1 == tag2
    # Try taging out the `__eq__` method in lib/tag.py
    # And see what happens when you run this test again.
