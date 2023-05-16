from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog.sql")

# Retrieve all artists
post_repository = PostRepository(connection)
posts = post_repository.all()

# List them out
for post in posts:
    print(post)

post_1 = post_repository.find_with_comments(1)

print("Comments of " + str(post_1))
print(post_1.comments)