class UserAccount():
    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.username}, {self.email}"