class Post():
    def __init__(self, id, title, content, number_of_views, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.number_of_views = number_of_views
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post Nr {self.id}: {self.title.capitalize()}. {self.content.capitalize()} by user {self.user_id}. Views: {self.number_of_views}"