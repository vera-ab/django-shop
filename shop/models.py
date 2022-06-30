from django.db import models
from django.contrib.postgres.fields import ArrayField


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=25)
    birth_date = models.DateField(blank=True, null=True)


class Movie(models.Model):
    MOVIE_TYPE = [('Short', 'Short-movie'), ('Movie', 'Movie')]

    imdb_id = models.CharField(max_length=255, null=True)
    title_type = models.CharField(max_length=255, choices=MOVIE_TYPE)
    name = models.CharField(max_length=255)
    is_adult = models.BooleanField(null=True)
    year = models.DateField(null=True)
    genres = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.name


class Person(models.Model):
    imdb_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birth_year = models.DateField(null=True)
    death_year = models.DateField(null=True)

    def __str__(self):
        return self.name


class PersonMovie(models.Model):
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE)
    person_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    order = models.IntegerField(null=True)
    category = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    characters = ArrayField(models.CharField(max_length=200), default=list)


