Two Tables Design Recipe Template

1. Extract nouns from the user stories or specification

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

Nouns:

user account, email address, username, posts, title, content, number of views


2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record	        Properties
user account	email address, username
post        	title, content, number of views

Name of the first table (always plural): user accounts

Column names: email address, username

Name of the second table (always plural): posts

Column names: title, content, number of views

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

Table: user accounts
id: SERIAL
email address: text
username: text

Table: posts
id: SERIAL
title: text
content: text
number of views: int


4. Decide on The Tables Relationship

Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

1. Can one user account have many posts? YES
2. Can one post have many user accounts? NO

-> Therefore,
-> A user account HAS MANY posts
-> A post BELONGS TO a user account

-> Therefore, the foreign key is on the posts table.

4. Write the SQL


file: social_network.sql

CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  number_of_views int,
-- The foreign key name is always {other_table_singular}_id
  user_account_id int,
  constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id)
    on delete cascade
);

5. Create the tables

psql -h 127.0.0.1 social_network < seeds/social_network.sql