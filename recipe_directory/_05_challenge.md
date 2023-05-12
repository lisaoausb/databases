Single Table Design Recipe Template

Copy this recipe template to design and create a database table from a specification.

1. Extract nouns from the user stories or specification

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).

nouns: recipes, name, average cooking time in minutes, rating from 1 to 5

2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
recipe	name, average_cooking_time, rating
Name of the table (always plural): recipes

Column names: name, average_cooking_time, rating

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

id: SERIAL
name: text
average_cooking_time: int
rating: int

4. Write the SQL

file: recipes.sql

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    average_cooking_time int
    rating int
);


5. Create the table

SKIP BECAUSE WE ARE USING A SEED FILE?

NOPE – still need to create a database. In the database_connection file we are connecting to it.

psql -h 127.0.0.1 recipe_directory < recipes.sql

--------------------------------------------------------------------------------------

RECIPES
Model and Repository Classes Design Recipe

1. Design and create the Table

See design above


2. Create Test SQL seeds

See table above // recipes.sql file

3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

Table name: recipes

Model class in lib/recipes.py
class Recipe

Repository class in lib/recipe_repository.py
class RecipeRepository

4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

table name: recipes
class Recipe
    def __init__(self):
        self.id = id
        self.name = name
        self.average_cooking_time = average_cooking_time
        self.rating = rating

in lib/recipe.py

5. Define the Repository Class interface

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

table name: recipes

Repository class
in lib/recipe_repositry.py

class RecipeRepository():
    def __init__(self):
    # Parameters: connection
    # Side effects: sets connection property
    pass

    def all(self, query):
    # Parameters: SQL query to query the database = SELECT * FROM recipes;
    # Returns: all recipes in database

    def find(self, recipe_id):
    # Parameters: SQL query, ID that I want to find SELECT * FROM recipes WHERE id = $1;
    # Returns: recipe stored in id specified

6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.


"""
Get all records from the recipes database
"""

repo = RecipeRepository()
recipes = repo.all()
recipes == [Recipe, Recipe, Recipe, Recipe, Recipe]


"""
Get a specific record based on its ID
"""

repo = RecipeRepository()
recipe = repo.find()
recipe == Recipe

7. Test-drive and implement the Repository class behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.