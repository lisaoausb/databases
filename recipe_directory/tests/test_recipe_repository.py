from lib.recipe_repository import *
from lib.recipe import *

"""
Get all records from the recipes database
"""

def test_all_records_returned(db_connection):
    repo = RecipeRepository(db_connection)
    recipes = repo.all()
    assert recipes == [Recipe(1, 'Paprika-Rahm-Schnitzel', 30, 4),
                Recipe(2, 'Kiachi', 75, 5),
                Recipe(3, 'Gemüsecurry', 30, 3),
                Recipe(4, 'Kaiserschmarrn', 45, 5),
                Recipe(5, 'Zimtschnecken', 120, 5)
                ]


"""
Get a specific record based on its ID
"""

def test_get_one_record(db_connection):
    repo = RecipeRepository(db_connection)
    recipe_4 = repo.find(4)
    assert recipe_4 == Recipe(4, 'Kaiserschmarrn', 45, 5)

# repo = RecipeRepository()
# recipe = repo.find()
# recipe == Recipe

def test_find_based_on_rating_5_stars(db_connection):
    repo = RecipeRepository(db_connection)
    recipes = repo.find_rating(5)
    assert recipes == [Recipe(2, 'Kiachi', 75, 5),
                Recipe(4, 'Kaiserschmarrn', 45, 5),
                Recipe(5, 'Zimtschnecken', 120, 5)
                ]