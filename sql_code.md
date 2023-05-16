03_querying_data 
challenge:

music_library=# SELECT title FROM albums WHERE release_year >= 1980 AND release_year <= 1990 AND artist_id = 1;

04_updating_data

Exercise:
music_library=# UPDATE albums SET release_year = 1972 WHERE id = 3;

Challenge:
DELETE FROM albums WHERE id = 12;

05_creating_new_data

Exercise: 
(1) INSERT INTO albums (title, release_year) VALUES('Mezzanine', 1998);
(2) UPDATE albums SET artist_id = 5 WHERE id = 13;

Challenge:
(1) INSERT INTO albums (title, release_year, artist_id) VALUES('This is Why', 2023, 6);

(2) INSERT INTO artists (name, genre) VALUES ('Paramore', 'Alternative Rock');

JOINS
Exercise 1
Using psql, use a JOIN query to select the id and title of all the albums from Taylor Swift.

SELECT albums.id, albums.title FROM albums JOIN artists ON albums.artist_id = artists.id WHERE artists.id = 3;

Exercise 2
Use a JOIN query to find the id and title of the (only) album from Pixies released in 1988.

SELECT albums.id, albums.title FROM albums JOIN artists ON albums.artist_id = artists.id WHERE albums.release_year = 1988 AND artists.name = 'Pixies';

Challenge
Find the album_id and title of all albums from Nina Simone released after 1975.

SELECT albums.id, albums.title FROM albums JOIN artists ON albums.artist_id = artists.id WHERE albums.release_year > 1975 AND artists.name = 'Nina Simone';
