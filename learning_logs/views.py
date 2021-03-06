from django.shortcuts import render, redirect # Redirect will send the user back to the topics page once the form is submitted
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry # we import this because the models.py file has data under a class called Topic
from .forms import TopicForm, EntryForm

# Create your views here.
# Functions below must match a path in the main app file. In this case learning_logs/urls.py; function views.index
def index(request):
    """ homepage for learning log. """
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """ Show all topics. """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # Here we store all the information from the class and object 'date_added' into another variable 'topics'
    context = {'topics': topics} # Here we define a context --> a key value pairing containing a set of topics from models.py
    return render(request, 'learning_logs/topics.html', context) # This is a standard render that will display the context, request, and house the file path

@login_required
def topic(request, topic_id): # whatever is captured in '/<int:topic_id>/' from urls.py will be stored in 'topic_id' function
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id) # We get the the topic and store it in an ID

    # Make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added') # we get the entries associated with the topic and order them by date_added. The '-' reverses the order
    context = {'topic': topic, 'entries': entries} # we store the topics and entries into context
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """ Add a new topic """
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """ Add a new entry for a particular topic """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted; create a blank form
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # if no data, use what is already in the entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
