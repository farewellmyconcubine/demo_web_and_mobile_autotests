from selene import browser, be
import allure


class MoviePage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, movie_name):
        with allure.step('Open Movie page'):
            browser.element(f'//*[text()="{movie_name.title()} "]').click()

    def add_to_watchlist(self):
        with allure.step('Add movie to watchlist'):
            browser.element('.-watchlist.add-to-watchlist').click()

    def assert_page_elements(self):
        with allure.step('Assert elements are present on the page'):
            browser.element('.headline-1').should(be.visible)
        browser.element('.trailer-link').should(be.visible)
        browser.element('.filmstat-watches').should(be.visible)
        browser.element('.filmstat-lists').should(be.visible)
        browser.element('.filmstat-likes').should(be.visible)
        browser.element('.ratings-histogram-chart').should(be.visible)
        browser.element('.related-films').should(be.visible)
