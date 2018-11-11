from .base import FunctionalTest


class EventListingTest(FunctionalTest):

    def test_can_view_a_list_of_events(self):

        # We need to add some events to the test database first
        self.add_test_event()

        # Bill browses to the events list page
        self.browser.get(f'{self.live_server_url}/events/')

        # He sees in the title that he is at the Events page
        self.assertEqual(self.browser.title, 'BandFollow - Events')

        # There is a table of events
        self.browser.find_element_by_id('id_list_table')

        # He sees the 'Big Night Out!' event in the table
        self.wait_for_row_in_table('Big Night Out! Super Rock Club March 22, 2019')

    def test_can_create_a_new_event(self):

        # We need to add an artist and venue first
        self.add_the_melons()
        self.add_super_rock_club()

        # We need to create Bill's account for the test database
        self.create_bill()

        # Bill wants to add a new event. He goes the add event page.
        self.browser.get(f'{self.live_server_url}/add_event/')

        # The browser redirects him to log in since he has not yet
        self.assertEqual(f'{self.live_server_url}/accounts/login/?next=/add_event/',
                         self.browser.current_url)

        # He logs in with his account
        self.browser.find_element_by_id('id_username').send_keys('bill')
        self.browser.find_element_by_id('id_password').send_keys('ILoveHatsDude!')
        self.browser.find_element_by_id('id_submit').click()

        # There is a form to add a new event.
        self.browser.find_element_by_id('id_add_event_form')
