class Recipe():
    def __init__(self, id, name, average_cooking_time, rating):
        self.id = id
        self.name = name
        self.average_cooking_time = average_cooking_time
        self.rating = rating

    def __repr__(self):
        return f'{self.name} takes {self.average_cooking_time} minutes and is rated {self.rating} stars.'
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__