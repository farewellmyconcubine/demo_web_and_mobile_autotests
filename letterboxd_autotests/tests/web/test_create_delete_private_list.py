from time import sleep
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.pages.lists_page import ListsPage
from letterboxd_autotests.tests.web.conftest import browser_setup

browser = browser_setup
login_page = LoginPage(browser)
lists_page = ListsPage(browser)
login = 'testingaccount1'
password = 'etsttest123~'
list_name = 'test list'

def test_create_private_list():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    lists_page.open(login)
    lists_page.initiate_list_creating()
    lists_page.fill_list_name(list_name)
    lists_page.change_list_privacy()
    lists_page.save_list()
    lists_page.open(login)
    lists_page.assert_list_creation(list_name)

def test_delete_private_list():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    lists_page.open(login)
    lists_page.delete_list(list_name)
    sleep(1)
    lists_page.assert_no_list_exist(list_name)