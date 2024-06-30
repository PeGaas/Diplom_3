import allure

from data_static import EMAIL_USER
from locators.forgot_password_page_locators import EMAIL, BUTTON_RECOVER, PASSWORD, SHOW_PASSWORD
from locators.home_page_locators import PERSONAL_ACCOUNT
from locators.login_page_locators import RECOVER_PASSWORD
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввести адрес электронной почты в поле Email')
    def input_email(self):
        self.input_text(EMAIL, EMAIL_USER)

    @allure.step('Нажать на Восстановить пароль')
    def click_button_recover(self):
        self.click_to_element(BUTTON_RECOVER)

    @allure.step('Ввести пароль в поле Пароль')
    def input_password(self, password):
        self.input_text(PASSWORD, password)

    @allure.step('Нажать на иконку глаза, чтобы увидеть пароль')
    def click_show_password(self):
        self.click_to_element(SHOW_PASSWORD)

    @allure.step('Нажать на Личный Кабинет')
    def click_to_personal_account(self):
        self.click_to_element(PERSONAL_ACCOUNT)

    @allure.step('Нажать кнопку Восстановить')
    def click_to_recover_password(self):
        self.click_to_element(RECOVER_PASSWORD)
