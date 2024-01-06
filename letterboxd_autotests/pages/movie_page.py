from selene import browser, have, be

class MoviePage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, movie_name):
        browser.element(f'//*[text()="{movie_name.title()} "]').click()

    def add_to_watchlist(self):
        browser.element('.-watchlist.add-to-watchlist').click()

    def assert_page_elements(self):
        browser.element('.headline-1').should(be.visible)
        browser.element('.trailer-link').should(be.visible)
        browser.element('.filmstat-watches').should(be.visible)
        browser.element('.filmstat-lists').should(be.visible)
        browser.element('.filmstat-likes').should(be.visible)
        browser.element('.ratings-histogram-chart').should(be.visible)
        browser.element('.related-films').should(be.visible)
