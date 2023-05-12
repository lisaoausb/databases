from lib.user_account import *

class UserAccountRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM user_accounts;")
        details = []
        for row in rows:
            detail = UserAccount(row['id'], row['email_address'], row['username'])
            details.append(detail)
        return details

    def find(self, user_account_id):
        rows = self._connection.execute("SELECT * FROM user_accounts WHERE id = %s;", [user_account_id])
        details = []
        for row in rows:
            detail = UserAccount(row['id'], row['email_address'], row['username'])
            details.append(detail)
        return details[0]
    
    def create(self, useraccount):
        self._connection.execute("INSERT INTO user_accounts (email_address, username) VALUES(%s, %s);", [useraccount.email, useraccount.username])

    def delete(self, user_account_id):
        self._connection.execute("DELETE FROM user_accounts WHERE id = %s", [user_account_id])

    def update(self, user):
        self._connection.execute("UPDATE user_accounts SET email_address = %s, username = %s WHERE id = %s;", [user.email, user.username, user.id])

