from datetime import time


class Articles:
    def __init__(self,image,description,url,title,author):
        self.image = image
        self.decription =description
        self.time= time
        self.url = url
        self.title = title
        self.author = author

class Sources:
    '''
    defines source objects
    '''
    
    def _init_(self,id,name,description,url,category,country,language):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country
        self.language = language