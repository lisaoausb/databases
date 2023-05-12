from lib.recipe import *

"""
When we create a new instance
we set the properties
"""

def test_initialises_with_properties():
    recipe = Recipe(1, 'recipe', 10, 1)
    assert recipe.id == 1
    assert recipe.name == 'recipe'
    assert recipe.average_cooking_time == 10
    assert recipe.rating == 1

def test_equliser():
    recipe1 = Recipe(1, 'recipe', 10, 1)
    recipe2 = Recipe(1, 'recipe', 10, 1)
    assert recipe1 == recipe2

def test_format():
    recipe = Recipe(1, 'recipe', 10, 1)
    assert str(recipe) == 'recipe takes 10 minutes and is rated 1 stars.'