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

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    poster = models.URLField(verbose_name="poster_url", default=None)

    def __repr__(self) -> str:
        return self.name.title()

    def __str__(self) -> str:
        return self.name.title()

    class Meta:
        verbose_name_plural = "Movies"

    def save(self):
        self.name = self.name.lower()
        super().save()