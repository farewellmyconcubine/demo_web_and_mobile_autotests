from selene import browser, have, be
import allure


class WatchlistPage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, login):
        with allure.step('Open Watchlist page'):
            browser.open(f'/{login}/watchlist')

    def assert_movie_is_present(self, movie_name):
        with allure.step('Assert movie is on the Watchlist'):
            browser.element('.film-poster').click()
        browser.element('.menu-link').click()
        browser.element('.popup-menu-text.-last').click()
        browser.element('.headline-1').should(have.text(movie_name.title()))

    def assert_watchlist_not_empty(self):
        with allure.step('Assert watchlist is not empty'):
            browser.element('.empty-text').should(have.no.existing)
        browser.element('[data-form-id="filmlist-reset"]').should(be.visible)

    def assert_watchlist_empty(self):
        with allure.step('Assert watchlist is empty'):
            browser.element('.empty-text').should(be.visible)

    def clear_watchlist(self, password):
        with allure.step('Clear watchlist'):
            browser.element('[data-form-id="filmlist-reset"]').click()
        browser.element('.field.-reversed[name="password"]').send_keys(password)
        browser.element('.-activity-indicator[type="submit"]').click()
