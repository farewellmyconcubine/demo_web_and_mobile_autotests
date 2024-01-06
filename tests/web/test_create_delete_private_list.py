from time import sleep
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.pages.lists_page import ListsPage
from tests.web.conftest import browser_setup
import os
import allure
from dotenv import load_dotenv
from get_env_path import get_personal_env_path
from get_env_path import get_test_data_path

browser = browser_setup
login_page = LoginPage(browser)
lists_page = ListsPage(browser)
load_dotenv(get_personal_env_path())
load_dotenv(get_test_data_path())
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
list_name = os.getenv('LIST_NAME')

@allure.epic('Lists page')
@allure.feature('Lists creation/deletion')
@allure.story('Create list')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Major')
def test_create_private_list():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    lists_page.open(login)
    lists_page.initiate_list_creation()
    lists_page.fill_list_name(list_name)
    lists_page.change_list_privacy()
    lists_page.save_list()
    lists_page.open(login)
    lists_page.assert_list_creation(list_name)

@allure.epic('Lists page')
@allure.feature('Lists creation/deletion')
@allure.story('Delete list')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Major')
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
