from .base import FunctionalTest


class EventListingTest(FunctionalTest):

    def test_can_view_a_list_of_events(self):

        # We need to add some events to the test database first
        self.add_test_events()
