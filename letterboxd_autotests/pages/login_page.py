from allure import step
from selene import browser, have, be

class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        browser.open('/sign-in')

    def fill_login(self, login):
        browser.element('#field-username').send_keys(login)

    def fill_password(self, password):
        browser.element('#field-password').send_keys(password)

    def sign_in(self):
        browser.element('button.standalone-flow-button[type="submit"]').click()

    def assert_log_in(self, login):
        browser.element('.nav-account').should(have.exact_text(login.upper()))
        browser.element('.title-hero a').should(have.exact_text(login))