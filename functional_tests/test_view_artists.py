from .base import FunctionalTest


class ArtistListingTest(FunctionalTest):

    def test_can_view_a_list_of_artists(self):

        # Bill doesn't have an account but just wants to browse artists
        self.browser.get(f'{self.live_server_url}/artists')

        # He sees in the title that he is at the Artists page
        self.assertEqual(self.browser.title, 'BandFollow - Artists')
