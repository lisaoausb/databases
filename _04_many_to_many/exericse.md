Two Tables Design Recipe Template

1. Extract nouns from the user stories or specification

As a coach
So I can get to know all students
I want to keep a list of students' names.

As a coach
So I can get to know all students
I want to assign tags to students (for example, "happy", "excited", etc).

As a coach
So I can get to know all students
I want to be able to assign the same tag to many different students.

As a coach
So I can get to know all students
I want to be able to assign many different tags to a student.

nouns: students, students' names, tags

2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
student	name, tag
tag	student
Name of the first table (always plural): students

Column names: name

Name of the second table (always plural): tags

Column names: name

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

Table: students
id: SERIAL
name: text

Table: tags
id: SERIAL
name: text


4. Design the Many-to-Many relationship

1. Can one tag have many students? YES
2. Can one student have many tags? YES

If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case.

5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is table1_table2.

students_tags
student_id
tag_id

# EXAMPLE

Join table for tables: posts and tags
Join table name: posts_tags
Columns: post_id, tag_id


4. Write the SQL.

file: students_tags.sql

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name text
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name text
);

-- Create the join table.
CREATE TABLE students_tags (
  student_id int,
  tag_id int,
  constraint fk_student foreign key(student_id) references students(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (student_id, tag_id)
);

5. Create the tables.

psql -h 127.0.0.1 students_tags < students_tags.sql