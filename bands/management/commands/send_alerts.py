from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from bands.models import Event

User = get_user_model()


class Command(BaseCommand):
    help = 'Cycles through events and will email any user that has both the artist and venue in their favorites.'

    def handle(self, *args, **options):

        for event in Event.objects.filter(date_and_time__gte=timezone.now()):
            artists = event.artists.all()
            venue = event.venue

            for user in User.objects.all():
                venue_match = False
                artist_match = False
                if venue in user.favorite_venues.all():
                    venue_match = True
                for artist in artists:
                    if artist in user.favorite_artists.all():
                        artist_match = True
                        break

                if venue_match and artist_match:
                    print('{} wants {}'.format(user.username, event.title))
