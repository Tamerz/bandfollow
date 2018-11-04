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
        self.wait_for_row_in_table('Big Night Out!')
