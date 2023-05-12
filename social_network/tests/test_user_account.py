from lib.user_account import *

def test_constructs():
    user = UserAccount(1, 'email', 'username')
    assert user.id == 1
    assert user.email == 'email'
    assert user.username == 'username'

def test_equaliser():
    user1 = UserAccount(1, 'email', 'username')
    user2 = UserAccount(1, 'email', 'username')
    assert user1 == user2

def test_format():
    user = UserAccount(1, 'email', 'username')
    assert str(user) == 'username, email'