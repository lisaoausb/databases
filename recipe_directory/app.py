from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes.sql")

# Retrieve all artists
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

# List them out
for recipe in recipes:
    print(recipe)

# Retrieve specific recipe
recipe_4 = recipe_repository.find(4)

# Print it
print(f"The recipe you were looking for is: {recipe_4}")

# Retrieve best recipes
best_recipes = recipe_repository.find_rating(5)

# List them out
for recipe in best_recipes:
    print(f"The best recipes are: {recipe}")