from selene import browser, have
import allure


class ListsPage():

    def __init__(self, browser):
        self.browser = browser

    def open(self, login):
        with allure.step('Open Lists page'):
            browser.open(f'/{login}/lists')

    def initiate_list_creation(self):
        with allure.step('Initiate list creation'):
            browser.element('.actions-panel').click()

    def fill_list_name(self, list_name):
        with allure.step('Fill list name'):
            browser.element('input[type="text"][name="name"]').send_keys(list_name)

    def change_list_privacy(self):
        with allure.step('Change list privacy'):
            browser.element('#frm-sharing-policy').click()
        browser.element('#frm-sharing-policy [value="You"]').click()

    def save_list(self):
        with allure.step('Save list'):
            browser.element('#list-edit-save.button-action.right').click()

    def delete_list(self, list_name):
        with allure.step('Delete list'):
            browser.element(f'//*[@class="film-list-summary"]//a[contains(text(), "{list_name}")]').click()
        browser.element('#userpanel a[rel="nofollow"]').click()
        browser.element('#delete-film-list').click()
        browser.element('.modal-ok').click()

    def assert_list_creation(self, list_name):
        with allure.step('Assert list is created'):
            browser.element(f'//*[@class="film-list-summary"]//a[contains(text(), "{list_name}")]').should(
                have.text(list_name))

    def assert_no_list_exist(self, list_name):
        with allure.step('Assert list is deleted'):
            browser.element(
                f'//*[@class="section col-17 col-main overflow"]//a[contains(text(), "{list_name}")]').should(
                have.no.existing)
