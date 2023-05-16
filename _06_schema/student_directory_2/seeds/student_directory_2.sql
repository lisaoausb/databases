
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS cohorts;

DROP SEQUENCE IF EXISTS students_id_seq;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE SEQUENCE IF NOT EXISTS students_id_seq;

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

INSERT INTO cohorts (name, starting_date) VALUES('April', '1/4/2023'), ('May', '1/5/2023');
INSERT INTO students (name, cohort_id) VALUES('Lisa', 1);
INSERT INTO students (name, cohort_id) VALUES('Rahul', 1);
INSERT INTO students (name, cohort_id) VALUES('Kate', 1);
INSERT INTO students (name, cohort_id) VALUES('Mama', 2);
INSERT INTO students (name, cohort_id) VALUES('Papa', 2);