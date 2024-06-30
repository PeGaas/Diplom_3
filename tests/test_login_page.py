import allure
from data_static import LOGIN_URL, PROFILE_URL, ORDER_HISTORY_URL
from locators.home_page_locators import PERSONAL_ACCOUNT
from pages.login_page import LoginPage
from conftest import chrome_driver


class TestLoginPage:
    @allure.title('Переход в «Личный кабинет»')
    @allure.description('Переход по клику на «Личный кабинет»')
    def test_move_personal_account(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.click_to_personal_account()
        login_page.wait_url_contains(LOGIN_URL)
        login_page.input_email()
        login_page.input_password()
        login_page.click_button_enter()
        login_page.wait_element_to_be_clickable(PERSONAL_ACCOUNT)
        login_page.click_to_personal_account()
        login_page.wait_url_contains(PROFILE_URL)

        assert login_page.get_current_url() == PROFILE_URL

    @allure.title('Переход в «История заказов»')
    @allure.description('Переход в раздел «История заказов»')
    def test_move_order_history(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.click_to_personal_account()
        login_page.wait_url_contains(LOGIN_URL)
        login_page.input_email()
        login_page.input_password()
        login_page.click_button_enter()
        login_page.wait_element_to_be_clickable(PERSONAL_ACCOUNT)
        login_page.click_to_personal_account()
        login_page.wait_url_contains(PROFILE_URL)
        login_page.click_to_order_history()
        login_page.wait_url_contains(ORDER_HISTORY_URL)

        assert login_page.get_current_url() == ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    @allure.description('Выход из аккаунта нажатием "Выход"')
    def test_logout_account(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.click_to_personal_account()
        login_page.wait_url_contains(LOGIN_URL)
        login_page.input_email()
        login_page.input_password()
        login_page.click_button_enter()
        login_page.wait_element_to_be_clickable(PERSONAL_ACCOUNT)
        login_page.click_to_personal_account()
        login_page.wait_url_contains(PROFILE_URL)
        login_page.click_to_exit_account()
        login_page.wait_url_contains(LOGIN_URL)

        assert login_page.get_current_url() == LOGIN_URL

