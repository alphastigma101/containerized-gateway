"""
    You can view the user manual from here: https://docs.djangoproject.com/en/5.0/topics/db/models/
    Which shows you how to fully utilize Django's model api method 
"""
from django.db import models

class User(models.Model):
    '''
        Represents a user in the application.
    '''
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Logging(models.Model):
    '''
        Represents a logging entry associated with a user.
    '''
    issue = models.CharField(max_length=30)
    date = models.CharField(max_length=8)  # Must be in valid date format
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.issue} - {self.user.username}'
