from .base import FunctionalTest


class TestFavoriting(FunctionalTest):

    def test_can_favorite_an_artist(self):
        # We need to add an artist to the test database first
        self.add_the_melons()

        # Bill browses to our site
        self.browser.get(f'{self.live_server_url}')

        # We need to create Bill's account for the test database
        self.create_bill()

        # Bill wants to add a favorite artist. He goes to the artist list page.
        self.browser.get(f'{self.live_server_url}/artists/')

        # There is a table of artists
        self.browser.find_element_by_id('id_list_table')

        # He sees his favorite band The Melons in the table.
        self.wait_for_row_in_table('The Melons')

        # He clicks on his favorite band's name in the table.
        self.browser.find_element_by_id('id_artist_name').click()

        # He clicks on the favorite button on the artist detail page
        self.browser.find_element_by_id('id_artist_favorite').click()

        # The browser redirects him to log in since he has not yet
        self.assertEqual(f'{self.live_server_url}/accounts/login/?next=/set_favorite_artist/',
                         self.browser.current_url)

        # He logs in with his account
        self.browser.find_element_by_id('id_username').send_keys('bill')
        self.browser.find_element_by_id('id_password').send_keys('ILoveHatsDude!')
        self.browser.find_element_by_id('id_submit').click()

        # The login redirects him back to the artist detail page
        self.assertEqual(self.browser.title, 'BandFollow - The Melons')
        self.assertEqual(self.browser.current_url, f'{self.live_server_url}/artists/The Melons')

        # He hasn't marked this artist as a favorite before
        favorite_artist_value = self.browser.find_element_by_id('id_artist_favorite')
        self.assertEqual(favorite_artist_value.boolean, False)

        # He marks the artist as a favorite
        self.browser.find_element_by_id('id_artist_favorite').click()

        # He goes to his account page
        self.browser.get(f'{self.live_server_url}/account/')

        # He clicks on a link for Favorite Artists
        self.browser.find_element_by_id('id_favorite_artists').click()

        # This takes him to a list view page called Favorite Artists
        self.assertEqual(self.browser.title, 'BandFollow - Favorite Artists')
        self.assertEqual(self.browser.current_url, f'{self.live_server_url}/favorite_artists')

        # There is a table of artists
        self.browser.find_element_by_id('id_list_table')

        # He sees his favorite band The Melons in the table.
        self.wait_for_row_in_table('The Melons')
