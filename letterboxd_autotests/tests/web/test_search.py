from letterboxd_autotests.tests.web.conftest import browser_setup
from letterboxd_autotests.pages.home_page import HomePage
from letterboxd_autotests.pages.search_page import SearchPage

def test_search():
    browser = browser_setup
    search_page = SearchPage(browser)
    home_page = HomePage(browser)
    movie_name = 'Farewell my concubine'

    home_page.open()
    search_page.search_movie(movie_name)
    search_page.assert_search_results(movie_name)