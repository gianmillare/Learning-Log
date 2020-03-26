""" Define URL Patterns for learning_logs """

from django.urls import path # dependency
from . import  views # importing the views module from the same directory as this file

app_name = 'learning_logs'
urlpatterns = [
    # This is where you would put all the paths for the app
    # Home page;
    path('', views.index, name='index'), # The first input is an empty string because it refers to the end of the URL
    # Because the home page url is 'http://127.0.0.1:8000/' there is no string at the end. Hence, it is empty.
    # Other URLs in this page will have a pattern at the end of the above URL

    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Path for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]