from django.db import models

# Create your models here.
class Topic(models.Model): # This is where we create the backbone. 'Model' is included with Django for model's functionality
    """ Topic the User is learning """

    text = models.CharField(max_length=200) # this attribure 'text' takes in characters via 'CharField'
    date_added = models.DateTimeField(auto_now_add=True) # this attribute passes the current data and time

    def __str__(self): # this will return a string attribute inputted from the text attribute
        """ Return a string representation of the model """
        return self.text

class Entry(models.Model):
    """ Something specific learned about a topic """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # This is how we connect a new entry to a previous class "Topic"
    # the on_delete=models.CASCADE will delete all entries if a topic is deleted; AKA 'cascading delete'
    text = models.TextField() # this does not have a size limit
    date_added = models.DateTimeField(auto_now_add=True) # this will present entries chronologically and timestamp them

    class Meta: # This tells Django that multiple entries will be called 'entries' instead of 'entrys'
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Return a string represenation of the model """
        return f"{self.text[:50]}..." # This tells Django that if there is more than 50 characters, it will be followed by an ellipses