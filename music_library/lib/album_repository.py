from lib.album import *


class AlbumRepository:
# establish a connection with database
    def __init__(self, connection):
        self._connection = connection

    # get a list of all albums
    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums