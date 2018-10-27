from .base import FunctionalTest


class VenueListingTest(FunctionalTest):

    def test_can_view_a_list_of_venues(self):

        # We need to add a venue to the test database first
        self.add_super_rock_club()

        # Bill doesn't have an account but just wants to browse venues
        self.browser.get(f'{self.live_server_url}/venues/')

        # He sees in the title that he is at the Venues page
        self.assertEqual(self.browser.title, 'BandFollow - Venues')

        # There is a table of venues
        self.browser.find_element_by_id('id_venues_table')

        # He sees his favorite venue Super Rock Club in the table.
        self.wait_for_row_in_table('Super Rock Club')
