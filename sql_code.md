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

