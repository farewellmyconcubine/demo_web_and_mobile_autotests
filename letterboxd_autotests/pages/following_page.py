from selene import browser, have
import allure


class FollowingPage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, login):
        with allure.step('Open following page'):
            browser.open(f'/{login}/following')

    def open_user_profile(self, user_login):
        with allure.step('Open user profile'):
            browser.open(f'/{user_login}')

    def follow_user(self):
        with allure.step('Follow user'):
            browser.element('.follow-button-wrapper').click()

    def unfollow_user(self):
        with allure.step('Unfollow user'):
            browser.element('.-following').click()

    def assert_following(self, user_login):
        with allure.step('Assert a user is followed'):
            browser.element(f'//*[@class="person-summary"]//a[contains(text(), "{user_login}")]').should(
                have.text(user_login))

    def assert_unfollow(self, user_login):
        with allure.step('Assert a user is unfollowed'):
            browser.element(f'//*[@class="person-summary"]//a[contains(text(), "{user_login}")]').should(
                have.no.text(user_login))
