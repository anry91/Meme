from datetime import datetime
from random import randint
class Meme:
    last_id = 1
    def __init__(self, title, author, rating):
        
        self.title =title
        self.author = author
        self.rating = rating
        self.published = datetime.now()
        self.id =Meme.last_id
        Meme.last_id +=1
        #self.id = randint(1, 1000000)
    def __str__(self):
        return f"MEME: '({self.id}){self.title}'\n\
            author: {self.author}\n\
            rating: {self.rating}\n\
            published: {self.published}"
            
    def __gt__(self, other):
        return self.rating > other.rating