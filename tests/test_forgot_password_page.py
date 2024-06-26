import allure
from data_static import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from locators.forgot_password_page_locators import CLASS_ACTIVE
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


class TestForgotPasswordPage:
    @allure.title('Проверить что работает переход на страницу восстановления пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_button_recovery_password(self, chrome_driver):
        login_page = LoginPage(chrome_driver)
        login_page.click_to_personal_account()
        login_page.click_to_recover_password()

        assert login_page.get_current_url() == FORGOT_PASSWORD_URL

    @allure.title('Проверить что работает кнопка Восстановить')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_button_recovery(self, chrome_driver):
        forgot_password_page = ForgotPasswordPage(chrome_driver)
        forgot_password_page.click_to_personal_account()
        forgot_password_page.click_to_recover_password()
        forgot_password_page.input_email()
        forgot_password_page.click_button_recover()
        forgot_password_page.wait_url_contains(RESET_PASSWORD_URL)

        assert forgot_password_page.get_current_url() == RESET_PASSWORD_URL

    @allure.title('Проверить что иконка "глазик" показывает/скрывает пароль')
    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_button_show_password_true(self, chrome_driver):
        forgot_password_page = ForgotPasswordPage(chrome_driver)
        forgot_password_page.click_to_personal_account()
        forgot_password_page.click_to_recover_password()
        forgot_password_page.input_email()
        forgot_password_page.click_button_recover()
        forgot_password_page.wait_url_contains(RESET_PASSWORD_URL)
        forgot_password_page.input_password()
        forgot_password_page.click_show_password()

        assert 'input_status_active' in forgot_password_page.find_element(CLASS_ACTIVE).get_attribute("class")
