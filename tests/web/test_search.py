from tests.web.conftest import browser_setup
from letterboxd_autotests.pages.home_page import HomePage
from letterboxd_autotests.pages.search_page import SearchPage
from dotenv import load_dotenv
from get_env_path import get_test_data_path
import os
import allure

browser = browser_setup
search_page = SearchPage(browser)
home_page = HomePage(browser)
load_dotenv(get_test_data_path())
movie_name = os.getenv('MOVIE_NAME')

@allure.epic('Search results')
@allure.feature('Search')
@allure.story('Movie search')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Critical')
def test_search():
    home_page.open()
    search_page.search_movie(movie_name)
    search_page.assert_search_results(movie_name)
