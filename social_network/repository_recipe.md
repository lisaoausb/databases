SOCIAL NETWORK
Model and Repository Classes Design Recipe

1. Design and create the Table

2. Create Test SQL seeds

3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

Table name: user accounts
Model class
(in lib/user_account.py)
class UserAccount

Repository class
(in lib/user_account_repository.py)
class UserAccountRepository

Table name: posts
Model class
(in lib/post.py)
class Post

Repository class
(in lib/post_repository.py)
class PostRepository

4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

Table name: user accounts
Model class
(in lib/user_account.py)

class UserAccount
    def __init__(self, email, username):
        self.email = email
        self.username = username

    def __eq__(self):
        pass
    
    def __repr__(self):
        pass

Repository class
(in lib/user_account_repository.py)

class UserAccountRepository
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        pass

    def find(self):
        pass
    
    def create(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

Table name: posts
Model class
(in lib/post.py)

class Post
    def __init__(self, title, content, number_of_views):
        self.title = title
        self.content = content
        self.number_of_views = number_of_views

    def __eq__(self):
        pass
    
    def __repr__(self):
        pass

Repository class
(in lib/post_repository.py)
class PostRepository
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        pass

    def find(self):
        pass
    
    def create(self):
        pass

    def delete(self):
        pass


5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class StudentRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    # 

    # def update(student)
    # 

    # def delete(student)
    # 
6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

# EXAMPLES

# 1
# Get all students

repo = StudentRepository()

students = repo.all()

len(students) # =>  2

students[0].id # =>  1
students[0].name # =>  'David'
students[0].cohort_name # =>  'April 2022'

students[1].id # =>  2
students[1].name # =>  'Anna'
students[1].cohort_name # =>  'May 2022'

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

student.id # =>  1
student.name # =>  'David'
student.cohort_name # =>  'April 2022'

# Add more examples for each method
Encode this example as a test.

7. Test-drive and implement the Repository class behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.