from time import sleep
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.pages.following_page import FollowingPage
from letterboxd_autotests.tests.web.conftest import browser_setup

browser = browser_setup
login_page = LoginPage(browser)
following_page = FollowingPage(browser)
login = 'testingaccount1'
password = 'etsttest123~'
list_name = 'test list'
user_name = 'someuser'

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