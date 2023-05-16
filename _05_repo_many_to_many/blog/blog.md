Two Tables Design Recipe Template

1. Extract nouns from the user stories or specification

As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

Nouns:

posts, posts' titles, posts' content, posts' comments, comments' content, comments' authors


2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record  	Properties
post	    title, content, comment
comment     content, author

Name of the first table (always plural): posts

Column names: title, content

Name of the second table (always plural): comments

Column names: content, author, post_id

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.


Table: posts
id: SERIAL
title: text
content: text

Table: comments
id: SERIAL
content: text
author: text
post_id: int

4. Decide on The Tables Relationship

Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one posts have many comments? YES
Can one comments have many posts? NO

Therefore,
a post HAS MANY comments
a comment BELONGS TO a post

Therefore, the foreign key is on the comments table.

4. Write the SQL

file: blog.sql

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title text,
    content text 
);
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    content text,
    author text,
    post_id int,
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

# If I delete a record of cohort (parent table), all student records in the students table
# (child table) will be deleted as well.

5. Create the tables

psql -h 127.0.0.1 blog < blog.sql