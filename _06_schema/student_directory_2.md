Two Tables Design Recipe Template

1. Extract nouns from the user stories or specification

As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

Nouns:

students, students' names, cohorts, cohorts' names, cohorts' starting dates, students' cohorts

2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

Record  	Properties
students	name, cohort
cohorts     name, starting_date
Name of the first table (always plural): cohort

Column names: name, starting_date

Name of the second table (always plural): students

Column names: name, cohort

3. Decide the column types

Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.


Table: cohorts
id: SERIAL
name: text
starting_date: text

Table: students
id: SERIAL
name: text
cohort_id: int

4. Decide on The Tables Relationship

Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
You'll then be able to say that:

[A] has many [B]
And on the other side, [B] belongs to [A]
In that case, the foreign key is in the table [B]

Can one students have many cohorts? NO
Can one cohorts have many students? YES

Therefore,
a cohort HAS MANY students
a student BELONGS TO a cohort

Therefore, the foreign key is on the students table.

4. Write the SQL

file: student_directory_2.sql

CREATE TABLE cohorts(
    id SERIAL PRIMARY KEY,
    name text,
    starting_date text 
);
CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name text,
    cohort_id int,
    constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

# If I delete a record of cohort (parent table), all student records in the students table
# (child table) will be deleted as well.

5. Create the tables

psql -h 127.0.0.1 student_directory_2 < student_directory_2.sql