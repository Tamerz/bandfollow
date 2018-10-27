from .base import FunctionalTest


class ArtistListingTest(FunctionalTest):

    def test_can_view_a_list_of_artists(self):

        # We need to add an artist to the test database first
        self.add_the_melons()

        # Bill doesn't have an account but just wants to browse artists
        self.browser.get(f'{self.live_server_url}/artists/')

        # He sees in the title that he is at the Artists page
        self.assertEqual(self.browser.title, 'BandFollow - Artists')

        # There is a table of artists
        self.browser.find_element_by_id('id_list_table')

        # He sees his favorite band The Melons in the table.
        self.wait_for_row_in_table('The Melons')

        # His second favorite band is local and less known, and is not currently in the list
        self.wait_for_row_in_table('Big Grant', inverse=True)

        # He sees a link to "Add an Artist"
        add_an_artist_link = self.browser.find_element_by_id('id_add_artist')
        self.assertEqual(add_an_artist_link.text, 'Add a new artist...')

    def test_can_add_new_artist(self):

        # We need to create Bill's account for the test database
        self.create_bill()

        # Bill wants to add a new artist. He goes the add artist page.
        self.browser.get(f'{self.live_server_url}/add_artist/')

        # The browser redirects him to log in since he has not yet
        self.assertEqual(f'{self.live_server_url}/accounts/login/?next=/add_artist/',
                         self.browser.current_url)

        # He logs in with his account
        self.browser.find_element_by_id('id_username').send_keys('bill')
        self.browser.find_element_by_id('id_password').send_keys('ILoveHatsDude!')
        self.browser.find_element_by_id('id_submit').click()

        # There is a form to add a new artist.
        self.browser.find_element_by_id('id_add_artist_form')

        # He enters the name of the artist into the form and clicks submit
        self.browser.find_element_by_id('id_artist_name').send_keys('Big Grant')
        self.browser.find_element_by_id('id_submit').click()

        # Since it still needs to be moderated, it doesn't show up in the list of artists yet
        self.wait_for_row_in_table('Big Grant', inverse=True)

        # We go ahead and mark it as approved and then it should now show up in the list
        self.mark_artist_approved('Big Grant')
        self.browser.get(f'{self.live_server_url}/artists/')
        self.wait_for_row_in_table('Big Grant')
