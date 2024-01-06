from tests.web.conftest import browser_setup
from letterboxd_autotests.pages.home_page import HomePage
from letterboxd_autotests.pages.search_page import SearchPage
from letterboxd_autotests.pages.movie_page import MoviePage
from dotenv import load_dotenv
from get_env_path import get_test_data_path
import os
import allure

browser = browser_setup
search_page = SearchPage(browser)
home_page = HomePage(browser)
movie_page = MoviePage(browser)
load_dotenv(get_test_data_path())
movie_name = os.getenv('MOVIE_NAME')

@allure.epic('Movie page')
@allure.feature('Movie page')
@allure.story('Movie page elements')
@allure.tag('web')
@allure.label('owner', 'farewellmyconcubine')
@allure.severity('Major')
def test_movie_page():
    home_page.open()
    search_page.search_movie(movie_name)
    movie_page.open(movie_name)
    movie_page.assert_page_elements()
