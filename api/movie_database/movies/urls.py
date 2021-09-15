from django.urls import path
from . import views

urlpatterns = [
    path("find/", views.FindMovie.as_view()),
    path("genres/", views.GetGenres.as_view())
]