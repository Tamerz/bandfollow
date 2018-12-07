from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class user(abstractuser):

    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_moderator = models.BooleanField(default=False)
    favorite_artists = models.ManyToManyField('Artist', blank=True)
    favorite_venues = models.ManyToManyField('Venue', blank=True)

    USERNAME_FIELD = 'username'


class Artist(models.Model):

    name = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    website = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('artist_detail', args=[str(self.name)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'artist'
        verbose_name_plural = 'artists'


class Venue(models.Model):

    name = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    website = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('venue_detail', args=[str(self.name)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'venue'
        verbose_name_plural = 'venues'


class Event(models.Model):

    title = models.CharField(max_length=200)
    date_and_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)
    artists = models.ManyToManyField('Artist')
    venue = models.ForeignKey('Venue', on_delete=models.PROTECT)

    @property
    def artist_list(self):
        return ','.join([artist.name for artist in self.artists.all()])

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.date_and_time}: {self.title}'

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'


class Alert(models.Model):

    event = models.ForeignKey('Event', on_delete=models.PROTECT, blank=True)
    user = models.ForeignKey('User', on_delete=models.PROTECT, blank=True)
    has_been_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.event.title} - {self.user.username}'
