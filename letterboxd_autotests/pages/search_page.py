from selene import browser, have, be

class SearchPage:

    def __init__(self, browser):
        self.browser = browser

    def open_search_widget(self):
        browser.element('.navitem .replace').click()

    def search_movie(self, movie_name):
        browser.element('#search-q').send_keys(movie_name).press_enter()


    def assert_search_results(self, movie_name):
        browser.element('.col-main .section-heading').should(have.text(f'matches for “{movie_name}”'.upper()))