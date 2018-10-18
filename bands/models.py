from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
