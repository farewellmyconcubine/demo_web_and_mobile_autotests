from selene import browser, have, be

class HomePage():

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        browser.open('/')