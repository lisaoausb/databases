Two Tables Design Recipe Template

1. Extract nouns from the user stories or specification

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of movies with their title and release date.

As a cinema company manager,
So I can keep track of movies being shown,
I want to keep a list of my cinemas with their city name (e.g 'London' or 'Manchester').

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which cinemas are showing a specific movie.

As a cinema company manager,
So I can keep track of movies being shown,
I want to be able to list which movies are being shown a specific cinema.

nouns: movies, title, release_date, cinemas, city_name

2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
movie	title, release_date
cinema	city_name
Name of the first table (always plural): movies

Column names: title, release_date

Name of the second table (always plural): cinemas

Column names: city_name

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

Table: movies
id: SERIAL
title: text
release_date: text

Table: cinemas
id: SERIAL
city_name: text


4. Design the Many-to-Many relationship

1. Can one tag have many students? YES
2. Can one student have many tags? YES

If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case.

5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is table1_table2.

movies_cinemas
movie_id
cinema_id

# EXAMPLE

Join table for tables: movies and cinemas
Join table name: movies_cinemas
Columns: movie_id, cinema_id


4. Write the SQL.

file: movies_cinemas.sql

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    release_date text
);

CREATE TABLE cinemas (
    id SERIAL PRIMARY KEY,
    city_name text
);

-- Create the join table.
CREATE TABLE movies_cinemas (
  movie_id int,
  cinema_id int,
  constraint fk_movie foreign key(movie_id) references movies(id) on delete cascade,
  constraint fk_cinema foreign key(cinema_id) references cinemas(id) on delete cascade,
  PRIMARY KEY (movie_id, cinema_id)
);

5. Create the tables.

psql -h 127.0.0.1 movies_cinemas < movies_cinemas.sql