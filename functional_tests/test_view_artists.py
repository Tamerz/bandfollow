from .base import FunctionalTest


class BandListingTest(FunctionalTest):

    def test_can_view_a_list_of_bands(self):

        self.browser.get('')
