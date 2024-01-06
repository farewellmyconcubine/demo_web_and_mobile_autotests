from time import sleep

from selene import browser, have, be

class WatchlistPage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, login):
        browser.open(f'/{login}/watchlist')

    def assert_movie_is_present(self, movie_name):
        browser.element('.film-poster').click()
        browser.element('.menu-link').click()
        browser.element('.popup-menu-text.-last').click()
        browser.element('.headline-1').should(have.text(movie_name.title()))

    def assert_watchlist_not_empty(self):
        browser.element('.empty-text').should(have.no.existing)
        browser.element('[data-form-id="filmlist-reset"]').should(be.visible)

    def assert_watchlist_empty(self):
        browser.element('.empty-text').should(be.visible)

    def clear_watchlist(self, password):
        browser.element('[data-form-id="filmlist-reset"]').click()
        browser.element('.field.-reversed[name="password"]').send_keys(password)
        browser.element('.-activity-indicator[type="submit"]').click()


