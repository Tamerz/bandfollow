from .base import FunctionalTest


class ArtistListingTest(FunctionalTest):

    def test_can_view_a_list_of_artists(self):

        ## We need to add an artist to the test database first
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