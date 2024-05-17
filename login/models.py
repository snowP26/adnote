import uuid
from django.db import models
from django.contrib.auth.models import User

def generate_shareable_link():
    return str(uuid.uuid4())
class YourModel(models.Model):
        @property
        def shareable_link(self):
            return generate_shareable_link()
class user(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

class notes(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Item(models.Model):
    notes = models.ForeignKey(notes, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)




    

