import pytest
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.tests.web.conftest import browser_setup

login = 'testingaccount1'
password = 'etsttest123~'

def test_login():

    browser = browser_setup
    login_page = LoginPage(browser)

    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()

    login_page.assert_log_in(login)