from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# # Connect to the database
# connection = DatabaseConnection()
# connection.connect()

# # Seed with some seed data
# connection.seed("seeds/music_library.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # List them out
# # for artist in artists:
# #     print(artist)

# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# for album in albums:
#     print(album)

# album = album_repository.find(3)
# print(f'We want to know what album ID 3 is. It is: {album}.')

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    print('Welcome to the music library manager!')
    print("What would you like to do? \n 1 - List all albums \n 2 - List all artists")
    selection = input('Enter your choice:\n')
    if selection == '1':
       album_repository = AlbumRepository(self._connection)
       albums = album_repository.all()
       print("Here is the list of albums:")
       for album in albums:
            print(f"{album.id} – {album.title}")

    elif selection == '2':
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()

        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")

    else: print('Not valid')

    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!

if __name__ == '__main__':
    app = Application()
    app.run()