from lib.post import *

class PostRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        records = self._connection.execute('SELECT * FROM posts')
        posts = []
        for record in records:
            record = Post(record['id'], record['title'], record['content'], record['number_of_views'], record['user_account_id'])
            posts.append(record)
        return posts

    def find(self, id):
        records = self._connection.execute('SELECT * FROM posts WHERE id = %s', [id])
        posts = []
        for record in records:
            record = Post(record['id'], record['title'], record['content'], record['number_of_views'], record['user_account_id'])
            posts.append(record)
        return posts[0]
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES(%s, %s, %s, %s)', [post.title, post.content, post.number_of_views, post.user_id])
        return None

    def delete(self, id):
        self._connection.execute('DELETE FROM posts WHERE id = %s', [id])
        return None
    
    def update(self, post):
        self._connection.execute('UPDATE posts SET title = %s, content = %s, number_of_views = %s, user_account_id = %s WHERE id = %s', [post.title, post.content, post.number_of_views, post.user_id, post.id])