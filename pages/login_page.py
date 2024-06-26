import allure

from data_generator import generate_email, generate_password
from locators.home_page_locators import PERSONAL_ACCOUNT
from locators.login_page_locators import RECOVER_PASSWORD, EMAIL, PASSWORD, BUTTON_ENTER, ORDER_HISTORY, EXIT_ACCOUNT
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать на Восстановить пароль')
    def click_to_recover_password(self):
        self.click_to_element(RECOVER_PASSWORD)

    @allure.step('Ввести адрес электронной почты в поле Email')
    def input_email(self):
        self.input_text(EMAIL, 'petergaas8126@yandex.ru')

    @allure.step('Ввести пароль в поле Пароль')
    def input_password(self):
        self.input_text(PASSWORD, '123456')

    @allure.step('Нажать на кнопку Войти')
    def click_button_enter(self):
        self.click_to_element(BUTTON_ENTER)

    @allure.step('Нажать на кнопку Лента Заказов')
    def click_to_order_history(self):
        self.click_to_element(ORDER_HISTORY)

    @allure.step('Нажать на Личный Кабинет')
    def click_to_personal_account(self):
        self.click_to_element(PERSONAL_ACCOUNT)

    @allure.step('Нажать на кнопку Выход')
    def click_to_exit_account(self):
        self.click_to_element(EXIT_ACCOUNT)
