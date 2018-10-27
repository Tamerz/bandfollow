from .base import FunctionalTest


class ArtistListingTest(FunctionalTest):

    def test_can_view_a_list_of_artists(self):

        # We need to add an artist to the test database first
        self.add_the_melons()

        # Bill doesn't have an account but just wants to browse artists
        self.browser.get(f'{self.live_server_url}/artists')

        # He sees in the title that he is at the Artists page
        self.assertEqual(self.browser.title, 'BandFollow - Artists')

        # There is a table of artists
        artist_table = self.browser.find_element_by_id('id_artist_table')

        # He sees his favorite band The Melons in the table.
        rows = artist_table.find_elements_by_tag_name('tr')
        self.assertIn('The Melons', [row.text for row in rows])

        # His second favorite band is local and less known, and is not currently in the list
        rows = artist_table.find_elements_by_tag_name('tr')
        self.assertNotIn('Big Grant', [row.text for row in rows])

        # He sees a link to "Add an Artist"
        add_an_artist_link = self.browser.find_element_by_id('id_add_artist')
        self.assertEqual(add_an_artist_link.text, 'Add a new artist...')

    def test_can_add_new_artist(self):

        # We need to create Bill's account for the test database
        self.create_bill()

        # Bill wants to add a new artist. He goes the add artist page.
        self.browser.get(f'{self.live_server_url}/add_artist')

        # The browser redirects him to log in since he has not yet
        self.assertEqual(f'{self.live_server_url}/accounts/login/?next=/add_artist',
                         self.browser.current_url)

        # He logs in with his account
        self.browser.find_element_by_id('id_username').send_keys('bill')
        self.browser.find_element_by_id('id_password').send_keys('ILoveHatsDude!')
        self.browser.find_element_by_id('id_submit').click()

        # There is a form to add a new artist.
        self.browser.find_element_by_id('id_add_artist_form')
