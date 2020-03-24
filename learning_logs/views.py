from django.shortcuts import render

# Create your views here.
# Functions below must match a path in the main app file. In this case learning_logs/urls.py; function views.index
def index(request):
    """ homepage for learning log. """
    return render(request, 'learning_logs/index.html')