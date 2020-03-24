from django.shortcuts import render

from .models import Topic # we import this because the models.py file has data under a class called Topic

# Create your views here.
# Functions below must match a path in the main app file. In this case learning_logs/urls.py; function views.index
def index(request):
    """ homepage for learning log. """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ Show all topics """
    topics = Topic.objects.order_by('date_added') # Here we store all the information from the class and object 'date_added' into another variable 'topics'
    context = {'topics': topics} # Here we define a context --> a key value pairing containing a set of topics from models.py
    return render(request, 'learning_logs/topics.html', context) # This is a standard render that will display the context, request, and house the file path