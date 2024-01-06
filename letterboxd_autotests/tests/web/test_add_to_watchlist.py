from time import sleep
from letterboxd_autotests.pages.login_page import LoginPage
from letterboxd_autotests.pages.search_page import SearchPage
from letterboxd_autotests.pages.movie_page import MoviePage
from letterboxd_autotests.pages.watchlist_page import WatchlistPage
from letterboxd_autotests.tests.web.conftest import browser_setup

browser = browser_setup
search_page = SearchPage(browser)
login_page = LoginPage(browser)
movie_page = MoviePage(browser)
watchlist_page = WatchlistPage(browser)
movie_name = 'Farewell my concubine'
login = 'testingaccount1'
password = 'etsttest123~'
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

def test_clear_watchlist():
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.sign_in()
    sleep(1)
    watchlist_page.open(login)
    watchlist_page.assert_watchlist_not_empty()
    watchlist_page.clear_watchlist(password)
    watchlist_page.assert_watchlist_empty()