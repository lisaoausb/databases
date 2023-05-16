from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student

"""
When we call CohortRepository#all
We get a list of Cohort objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/student_directory_2.sql") # Seed our database with some test data
    repository = CohortRepository(db_connection) # Create a new ArtistRepository

    cohorts = repository.all() # Get all artists

    # Assert on the results
    assert cohorts == [
        Cohort(1, "April", "1/4/2023"),
        Cohort(2, "May", "1/5/2023")
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.find(1)
    assert cohort == Cohort(1, "April", "1/4/2023")

"""
When we call CohortRepository#find_with_students
we find a cohort we indicate and get a list of all
the students in this cohort
"""

def test_get_single_cohort_and_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)

    cohort = repository.find_with_students(1)
    assert cohort == Cohort(1, "April", "1/4/2023", [Student(1, 'Lisa', 1), Student(2, "Rahul", 1), Student(3, "Kate", 1)])


# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = ArtistRepository(db_connection)

#     repository.create(Artist(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(3, "Taylor Swift", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#         Artist(5, "The Beatles", "Rock"),
#     ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/student_directory_2.sql")
#     repository = ArtistRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#     ]
