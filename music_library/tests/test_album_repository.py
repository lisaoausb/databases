from lib.album_repository import *
from lib.album import *
"""
When we call AlbumRepository#all,
we get a list of all albums in seed database.
"""

def test_get_all_album_records(db_connection):
    db_connection.seed('seeds/music_library.sql')
    library = AlbumRepository(db_connection)

    albums = library.all() # get all albums

    assert len(albums) == 12

    assert albums[0].id == 1
    assert albums[0].title == 'Doolittle'
    assert albums[0].release_year == 1989
    assert albums[0].artist_id == 1

    assert albums[8].id == 9
    assert albums[8].title == 'Baltimore'
    assert albums[8].release_year == 1978
    assert albums[8].artist_id == 4
