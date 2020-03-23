from django.db import models

# Create your models here.
class Topic(models.Model): # This is where we create the backbone. 'Model' is included with Django for model's functionality
    """ Topic the User is learning """

    text = models.CharField(max_length=200) # this attribure 'text' takes in characters via 'CharField'
    date_added = models.DateTimeField(auto_now_add=True) # this attribute passes the current data and time

    def __str__(self): # this will return a string attribute inputted from the text attribute
        """ Return a string representation of the model """
        return self.text