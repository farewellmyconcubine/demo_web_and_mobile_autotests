from letterboxd_autotests.pages.login_page import LoginPage
from tests.web.conftest import browser_setup
import os
from dotenv import load_dotenv
from get_env_path import get_personal_env_path
import allure

browser = browser_setup
login_page = LoginPage(browser)
load_dotenv(get_personal_env_path())
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

@allure.epic('Login page')
@allure.feature('User log in')
@allure.story('Login')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Critical')
def test_login():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    login_page.assert_log_in(login)
