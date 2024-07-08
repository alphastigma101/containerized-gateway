"""
    You can view the user manual from here: https://docs.djangoproject.com/en/5.0/topics/db/models/
    Which shows you how to fully utilize Django's model api method 
"""
from django.db import models

class User(models.Model):
    '''
    Represents a database table containing user entries for this application.

    Fields:
        username (CharField): The username of the user.

    Methods:
        __str__: Returns the username as the string representation of the user object.
    '''

    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username
    
    class Meta:
        '''
        Defines metadata options for the User model.

        Attributes:
            db_table (str): Specifies the database table name for the User model.
                Additional options can be configured within this Meta class.
                For more information, refer to:
                https://docs.djangoproject.com/en/5.0/ref/models/options/#table-names
        '''
        db_table = "user"

class Report(models.Model):
    '''
        Represents a bug report Database table containing entries associated with the user.
        
        Fields:
            issue (CharField): The issue that occured during app's runtime
            date (CharField): The exact date the issue occured
            user (CharField): The bug report associated with the user 

        Methods:
            __str__: Returns the issue and the user that reported it 
    '''
    issue = models.CharField(max_length=30)
    date = models.CharField(max_length=8)  # Must be in valid date format
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.issue} - {self.user.username}'
    
    class Meta:
        '''
        Defines metadata options for the Report model.

        Attributes:
            db_table (str): Specifies the database table name for the User model.
                Additional options can be configured within this Meta class.
                For more information, refer to:
                https://docs.djangoproject.com/en/5.0/ref/models/options/#table-names
        '''
        db_table = "report"

class System(models.Model):
    '''
        Represents a System Database Table meant for logging entries.

        Fields:
            issue (CharField): The issue that occured during app's runtime
            date (CharField): The exact date the issue occured
            close (CharField): The exact date when to close the report            

    '''
    issue = models.CharField(max_length=30)
    date = models.CharField(max_length=8)  # Must be in valid date format
    close = models.CharField(max_length=8) # Must be set a week of system crash
    class Meta:
        '''
        Defines metadata options for the System model.

        Attributes:
            db_table (str): Specifies the database table name for the User model.
                Additional options can be configured within this Meta class.
                For more information, refer to:
                https://docs.djangoproject.com/en/5.0/ref/models/options/#table-names
        '''
        db_table = "system"


class Data(models.Model):
    '''
        Represents a Generic Database Table. Meant to be used if the user does not have a database

        Fields:
            None
    '''
    class Meta:
        '''
        Defines metadata options for the Data model.

        Attributes:
            db_table (str): Specifies the database table name for the User model.
                Additional options can be configured within this Meta class.
                For more information, refer to:
                https://docs.djangoproject.com/en/5.0/ref/models/options/#table-names
        '''
        db_table = "data"
