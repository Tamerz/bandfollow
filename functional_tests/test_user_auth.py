import time

from .base import FunctionalTest


class NewUserTest(FunctionalTest):

    def test_can_create_account(self):

        # Jimmy learned about a website that can let him get notified if a band he likes plays in venues near him.
        # He visits the site to check it out
        self.browser.get(self.live_server_url)

        # He sees the name of it is BandFollow
        self.assertIn('BandFollow', self.browser.title)

        # There is also a header with BandFollow
        self.assertIn('BandFollow', self.browser.find_element_by_tag_name('h1').text)

        # There is a link to create an account. He clicks it.
        create_account_link = self.browser.find_element_by_id('id_sign_up')
        self.assertEqual(create_account_link.text, 'Sign Up')
        create_account_link.click()

        # It takes him to the account creation page
        create_account_page = self.browser.current_url
        self.assertEqual(f'{self.live_server_url}/create_account/', create_account_page)

        # There is a form asking for user details. He fills it out with his information.
        self.browser.find_element_by_id('id_username').send_keys('jjazz')
        self.browser.find_element_by_id('id_name').send_keys('Jimmy Jazz')
        self.browser.find_element_by_id('id_email').send_keys('jimmy.jazz@tamerz.com')
        self.browser.find_element_by_id('id_password1').send_keys('youneverknow8')
        self.browser.find_element_by_id('id_password2').send_keys('youneverknow8')

        # He then sees the submit button and clicks it
        self.browser.find_element_by_id('submit-id-submit').click()

        # He now sees that he needs to click a link in his email to confirm it is valid
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertEqual(page_text, 'Please confirm your email address to complete the registration')

    def test_can_login(self):
        # New tests create new databases, so we need to create Jimmy again with
        # a helper method
        self.create_jimmy()

        # He goes back to the main site
        self.browser.get(self.live_server_url)

        # He clicks the "Log In" button
        login_link = self.browser.find_element_by_id('id_login')
        self.assertEqual(login_link.text, 'Log In')
        login_link.click()

        # He is now at the login page
        login_page = self.browser.current_url
        self.assertEqual(f'{self.live_server_url}/accounts/login/', login_page)

        # There is a login form that he fills out
        self.browser.find_element_by_id('id_username').send_keys('jjazz')
        self.browser.find_element_by_id('id_password').send_keys('youneverknow8')

        # He click the login button
        self.browser.find_element_by_id('id_submit').click()

        # He is redirected to the home page and sees a "Log Out" link.
        self.assertEqual(f'{self.live_server_url}/', self.browser.current_url)
        log_out_link = self.browser.find_element_by_id('id_log_out')
        self.assertEqual('Log Out', log_out_link.text)
