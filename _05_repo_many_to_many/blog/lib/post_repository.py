from lib.post import *
from lib.tag import *

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all cohorts
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"])
            posts.append(item)
        return posts

    # Find a single cohort by their id
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"])

    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            "SELECT posts.id as post_id, posts.title, posts.content AS post_content, comments.id AS comment_id, comments.content AS comment_content, comments.author FROM posts JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s;", [post_id])
        comments = []
        for row in rows:
            comment = Comment(row["comment_id"], row["comment_content"], row["author"], row['post_id'])
            comments.append(comment)

        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)

    def find_by_tag(self, tag):
        rows = self._connection.execute('SELECT posts.id, posts.title FROM posts JOIN posts_tags ON posts.id = posts_tags.post_id JOIN tags ON posts_tags.tag_id = tags.id WHERE tags.name = %s', [tag])
        tagged_posts = []
        for row in rows:
            tagged_post = Post(row['id'], row['title'])
            tagged_posts.append(tagged_post)

        return tagged_posts
    
    def find_by_post(self, post_id):
        rows = self._connection.execute('SELECT tags.id, tags.name FROM tags JOIN posts_tags ON tags.id = posts_tags.tag_id JOIN posts ON posts_tags.post_id = posts.id WHERE posts.id = %s;', [post_id])
        tags = []
        for row in rows:
            tag = Tag(row['id'], row['name'])
            tags.append(tag)

        return tags