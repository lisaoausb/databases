from lib.cohort import Cohort

"""
cohort constructs with an id, name and starting_date
"""
def test_cohort_constructs():
    cohort = Cohort(1, "test cohort", "test starting date")
    assert cohort.id == 1
    assert cohort.name == "test cohort"
    assert cohort.starting_date == "test starting date"

"""
We can format cohorts to strings nicely
"""
def test_cohorts_format_nicely():
    cohort = Cohort(1, "test cohort", "test starting_date")
    assert str(cohort) == "Cohort(1, test cohort, test starting_date)"
    # Try commenting out the `__repr__` method in lib/cohort.py
    # And see what happens when you run this test again.

"""
We can compare two identical cohorts
And have them be equal
"""
def test_cohorts_are_equal():
    cohort1 = Cohort(1, "Test cohort", "Test starting_date")
    cohort2 = Cohort(1, "Test cohort", "Test starting_date")
    assert cohort1 == cohort2
    # Try commenting out the `__eq__` method in lib/cohort.py
    # And see what happens when you run this test again.
