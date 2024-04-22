from datetime import datetime
class User:
    last_id = 1
    def __init__(self,name,email,password):
        if (" " in name) is False:
            self.name = name
        else:
            
            raise ValueError('dont use space character in name')
        if email[-10:] == '@gmail.com':

            self.email    = email
        elif email[-10:]  == '@yahoo.com':
            self.email = email
        else: 
            raise ValueError('Wrong email address')
        self.password = password
        self.created = datetime.now()
        self.id = User.last_id
        User.last_id += 1
    
    def __str__(self):
        return f"USER: {self.name} ({self.email})"