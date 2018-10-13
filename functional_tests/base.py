import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from bands.models import User, Artist


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    @staticmethod
    def createJimmy():
        jimmy = User()
        jimmy.username = 'jjazz'
        jimmy.name = 'Jimmy Jazz'
        jimmy.email = 'jimmy.jazz@coolguy.com'
        jimmy.set_password('youneverknow8')
        jimmy.save()

    @staticmethod
    def add_the_melons():
        the_melons = Artist()
        the_melons.name = 'The Melons'
        the_melons.save()
