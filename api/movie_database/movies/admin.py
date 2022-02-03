from django.contrib import admin
from .models import Genre, Director, Movie, Poster


admin.site.register([Genre, Director, Movie, Poster])