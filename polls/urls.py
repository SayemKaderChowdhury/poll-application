from django.urls import path

from . import views

# The URL declarations for this Django project;
# a “table of contents” of your Django-powered site
urlpatterns = [
    path("", views.index, name="index")
]
