from posixpath import dirname
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Genres"

    def __repr__(self) -> str:
        return self.name.title()

    def __str__(self) -> str:
        return self.name.title()


class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Directors"

    def __repr__(self) -> str:
        return self.name.title()

    def __str__(self) -> str:
        return self.name.title()

    def save(self):
        self.name = self.name.title()
        super().save()


class Poster(models.Model):
    path = models.FileField(max_length=500, null=True, upload_to="p")


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __repr__(self) -> str:
        return self.name.title()

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name_plural = "Languages"

    def save(self):
        self.name = self.name.title()
        super().save()


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre, unique=False)
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)
    description = models.TextField(max_length=900, null=True)
    score_imdb  = models.IntegerField(null=True)
    score_rotten_tomatoes_critic = models.IntegerField(null=True)
    score_rotten_tomatoes_audience = models.IntegerField(null=True)
    score_metacritic_viewer = models.FloatField(null=True)
    score_metacritic_critic = models.FloatField(null=True)
    imdb_id = models.CharField(max_length=100, null=True)
    tmdb_id = models.IntegerField(null=True)
    adult = models.BooleanField(null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    vote_count_imdb = models.CharField(max_length=100, null=True)
    vote_count_metacritic_viewer = models.CharField(max_length=100, null=True)
    vote_count_metacritic_critic = models.CharField(max_length=100, null=True)

    def __repr__(self) -> str:
        return self.name.title()

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name_plural = "Movies"

    def save(self):
        self.name = self.name.lower()
        super().save()


class Actor(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie)

    def __repr__(self) -> str:
        return self.name.title()

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name_plural = "Actors"

    def save(self):
        self.name = self.name.lower()
        super().save()




