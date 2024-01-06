from time import sleep
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.pages.following_page import FollowingPage
from tests.web.conftest import browser_setup
import os
import allure
from dotenv import load_dotenv
from get_env_path import get_personal_env_path
from get_env_path import get_test_data_path

browser = browser_setup
login_page = LoginPage(browser)
following_page = FollowingPage(browser)
load_dotenv(get_personal_env_path())
load_dotenv(get_test_data_path())
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
user_name = os.getenv('USER_NAME')

@allure.epic('Following Page')
@allure.feature('Following users')
@allure.story('Follow user')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Major')
def test_follow_user():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    following_page.open_user_profile(user_name)
    following_page.follow_user()
    following_page.open(login)
    following_page.assert_following(user_name)

@allure.epic('Following Page')
@allure.feature('Following users')
@allure.story('Unfollow user')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Major')
def test_unfollow_user():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    following_page.open_user_profile(user_name)
    following_page.unfollow_user()
    following_page.open(login)
    following_page.assert_unfollow(user_name)
