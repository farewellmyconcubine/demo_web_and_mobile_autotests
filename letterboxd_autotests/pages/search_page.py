from selene import browser, have
import allure


class SearchPage:

    def __init__(self, browser):
        self.browser = browser

    def open_search_widget(self):
        with allure.step('Open search widget'):
            browser.element('.navitem .replace').click()

    def search_movie(self, movie_name):
        with allure.step('Search query'):
            browser.element('#search-q').send_keys(movie_name).press_enter()

    def assert_search_results(self, movie_name):
        with allure.step('Assert search results'):
            browser.element('.col-main .section-heading').should(
                have.text(f'matches for “{movie_name}”'.upper()).or_(have.text('NO RESULTS')))
