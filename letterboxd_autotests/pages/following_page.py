from selene import browser, have, be

class FollowingPage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, login):
        browser.open(f'/{login}/following')

    def open_user_profile(self, user_login):
        browser.open(f'/{user_login}')

    def follow_user(self):
        browser.element('.follow-button-wrapper').click()

    def unfollow_user(self):
        browser.element('.-following').click()

    def assert_following(self, user_login):
        browser.element(f'//*[@class="person-summary"]//a[contains(text(), "{user_login}")]').should(have.text(user_login))

    def assert_unfollow(self, user_login):
        browser.element(f'//*[@class="person-summary"]//a[contains(text(), "{user_login}")]').should(have.no.text(user_login))
