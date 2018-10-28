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
        self.browser.find_element_by_id('id_list_table')

        # He sees his favorite venue Super Rock Club in the table.
        self.wait_for_row_in_table('Super Rock Club')

        # His second favorite venue 'Little Jazz Room' is not in the list
        self.wait_for_row_in_table('Little Jazz Room', inverse=True)

        # He sees a link to "Add a Venue"
        add_a_venue_link = self.browser.find_element_by_id('id_add_venue')
        self.assertEqual(add_a_venue_link.text, 'Add a new venue...')

    def test_can_add_new_venue(self):

        # We need to create Bill's account for the test database
        self.create_bill()

        # Bill wants to add a new venue. He goes the add venue page.
        self.browser.get(f'{self.live_server_url}/add_venue/')

        # The browser redirects him to log in since he has not yet
        self.assertEqual(f'{self.live_server_url}/accounts/login/?next=/add_venue/',
                         self.browser.current_url)

        # He logs in with his account
        self.browser.find_element_by_id('id_username').send_keys('bill')
        self.browser.find_element_by_id('id_password').send_keys('ILoveHatsDude!')
        self.browser.find_element_by_id('id_submit').click()

        # There is a form to add a new venue.
        self.browser.find_element_by_id('id_add_venue_form')

        # He enters the name of the venue into the form and clicks submit
        self.browser.find_element_by_id('id_venue_name').send_keys('Little Jazz Room')
        self.browser.find_element_by_id('id_submit').click()

        # Since it still needs to be moderated, it doesn't show up in the list of artists yet
        self.wait_for_row_in_table('Little Jazz Room', inverse=True)

        # We go ahead and mark it as approved and then it should now show up in the list
        self.mark_venue_approved('Little Jazz Room')
        self.browser.get(f'{self.live_server_url}/venues/')
        self.wait_for_row_in_table('Little Jazz Room')
