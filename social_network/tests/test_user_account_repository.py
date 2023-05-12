from lib.user_account_repository import *
from lib.user_account import *

"""
When I call UserRepsository#all, 
I get all records of database
"""

def test_all_records(db_connection):
    repo = UserAccountRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    details = repo.all()
    assert details == [
        UserAccount(1, 'test@gmail.com', 'test'),
        UserAccount(2, 'seed@gmail.com', 'seed'),
        UserAccount(3, 'social@gmail.com', 'social'),
    ]

"""
When I call UserRepository#find, 
I get the record of a specific id that I specify when calling.
"""

def test_find(db_connection):
    repo = UserAccountRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    my_account = repo.find(2)
    assert my_account == UserAccount(2, 'seed@gmail.com', 'seed')

"""
When I call UserRepository#create,
a new record is created and added to my database
based on what I specify
"""

def test_create(db_connection):
    repo = UserAccountRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    new_account = UserAccount(None, 'new@gmail.com', 'new')
    repo.create(new_account)
    details = repo.all()
    assert details == [
        UserAccount(1, 'test@gmail.com', 'test'),
        UserAccount(2, 'seed@gmail.com', 'seed'),
        UserAccount(3, 'social@gmail.com', 'social'),
        UserAccount(4, 'new@gmail.com', 'new')
    ]

"""
When I call UserRepository#delete,
an existing record is removed from my database
based on what I specify
"""

def test_delete(db_connection):
    repo = UserAccountRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    repo.delete(3)
    details = repo.all()
    assert details == [
        UserAccount(1, 'test@gmail.com', 'test'),
        UserAccount(2, 'seed@gmail.com', 'seed')
    ]

"""
When I call UserRepository#update,
an existing record gets updated in my database
based on what I specify
"""

def test_update(db_connection):
    repo = UserAccountRepository(db_connection)
    db_connection.seed('seeds/social_network.sql')
    user = repo.find(3)
    user.email = 'network@gmail.com'
    repo.update(user)
    details = repo.find(3)
    assert details == UserAccount(3, 'network@gmail.com', 'social')
