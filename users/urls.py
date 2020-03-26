""" Defines urls for users """

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # We add in default admin urls
    path('', include('django.contrib.auth.urls')),
]