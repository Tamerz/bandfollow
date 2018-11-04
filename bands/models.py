from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Venue(models.Model):

    name = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Event(models.Model):

    title = models.CharField(max_length=200)
    date_and_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    artists = models.ManyToManyField('Artist')
    venue = models.ForeignKey('Venue', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.date_and_time}: {self.title}'
