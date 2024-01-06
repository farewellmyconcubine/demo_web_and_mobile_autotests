from selene import browser
import allure


class HomePage():

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        with allure.step('Open Home Page'):
            browser.open('/')
