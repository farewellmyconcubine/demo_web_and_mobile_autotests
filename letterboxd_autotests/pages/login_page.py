from selene import browser, have
import allure


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        with allure.step('Open login page'):
            browser.open('/sign-in')

    def fill_login(self, login):
        with allure.step('Fill login'):
            browser.element('#field-username').send_keys(login)

    def fill_password(self, password):
        with allure.step('Fill password'):
            browser.element('#field-password').send_keys(password)

    def sign_in(self):
        with allure.step('Click Submit button'):
            browser.element('button.standalone-flow-button[type="submit"]').click()

    def assert_log_in(self, login):
        with allure.step('Assert user is logged in'):
            browser.element('.nav-account').should(have.exact_text(login.upper()))
        browser.element('.title-hero a').should(have.exact_text(login))
