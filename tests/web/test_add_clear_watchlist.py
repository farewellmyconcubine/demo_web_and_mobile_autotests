from time import sleep
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.pages.search_page import SearchPage
from letterboxd_autotests.pages.movie_page import MoviePage
from letterboxd_autotests.pages.watchlist_page import WatchlistPage
from tests.web.conftest import browser_setup
import os
import allure
from dotenv import load_dotenv
from get_env_path import get_personal_env_path
from get_env_path import get_test_data_path

browser = browser_setup
search_page = SearchPage(browser)
login_page = LoginPage(browser)
movie_page = MoviePage(browser)
watchlist_page = WatchlistPage(browser)
load_dotenv(get_personal_env_path())
load_dotenv(get_test_data_path())
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
movie_name = os.getenv('MOVIE_NAME')

@allure.epic('Watchlist page')
@allure.feature('Watchlist')
@allure.story('Add movie to watchlist')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Major')
def test_add_movie_to_watchlist():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    search_page.open_search_widget()
    search_page.search_movie(movie_name)
    movie_page.open(movie_name)
    movie_page.add_to_watchlist()
    watchlist_page.open(login)
    watchlist_page.assert_movie_is_present(movie_name)

@allure.epic('Watchlist page')
@allure.feature('Watchlist')
@allure.story('Clear watchlist')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Minor')
def test_clear_watchlist():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    watchlist_page.open(login)
    watchlist_page.assert_watchlist_not_empty()
    watchlist_page.clear_watchlist(password)
    sleep(1)
    watchlist_page.assert_watchlist_empty()
