import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from datetime import datetime

from bands.models import Artist, Venue, Event
User = get_user_model()


MAX_WAIT = 10


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    @staticmethod
    def create_jimmy():
        jimmy = User()
        jimmy.username = 'jjazz'
        jimmy.name = 'Jimmy Jazz'
        jimmy.email = 'jimmy.jazz@coolguy.com'
        jimmy.set_password('youneverknow8')
        jimmy.save()

    @staticmethod
    def create_bill():
        bill = User()
        bill.username = 'bill'
        bill.name = 'Bill Williamson'
        bill.email = 'bill@billshats.com'
        bill.set_password('ILoveHatsDude!')
        bill.save()

    @staticmethod
    def add_the_melons():
        the_melons = Artist()
        the_melons.name = 'The Melons'
        the_melons.is_approved = True
        the_melons.save()

    @staticmethod
    def add_super_rock_club():
        super_rock_club = Venue()
        super_rock_club.name = 'Super Rock Club'
        super_rock_club.is_approved = True
        super_rock_club.save()

    @wait
    def wait_for_row_in_table(self, row_text, inverse=False):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        if not inverse:
            self.assertIn(row_text, [row.text for row in rows])
        else:
            self.assertNotIn(row_text, [row.text for row in rows])

    @staticmethod
    def mark_artist_approved(artist_name):
        artist = Artist.objects.get(name=artist_name)
        artist.is_approved = True
        artist.save()

    @staticmethod
    def mark_venue_approved(venue_name):
        venue = Venue.objects.get(name=venue_name)
        venue.is_approved = True
        venue.save()

    @staticmethod
    def add_test_event():
        FunctionalTest.add_super_rock_club()
        FunctionalTest.add_the_melons()
        artist = Artist.objects.get(name='The Melons')
        venue = Venue.objects.get(name='Super Rock Club')
        event = Event()
        event.date_and_time = datetime(2019, 3, 22, 18, 30, tzinfo=timezone.utc)
        event.title = 'Big Night Out!'
        event.venue = venue
        event.save()
        event.artists.add(artist)
        event.is_approved = True
        event.save()
