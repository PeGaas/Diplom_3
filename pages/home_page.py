import allure
from locators.home_page_locators import PERSONAL_ACCOUNT, ORDER_FEED, INGREDIENT, MODAL_CLOSE, BUTTON_PLACE_ORDER
from locators.login_page_locators import EMAIL, PASSWORD, BUTTON_ENTER
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать на Личный Кабинет')
    def click_to_personal_account(self):
        self.click_to_element(PERSONAL_ACCOUNT)

    @allure.step('Нажать на Лента Заказов')
    def click_to_order_feed(self):
        self.click_to_element(ORDER_FEED)

    @allure.step('Нажать на ингридиент')
    def click_to_ingredient(self):
        self.click_to_element(INGREDIENT)

    @allure.step('Закрыть окно с детальным описанием ингридиента')
    def click_to_close_modal_ingredient_detail(self):
        self.click_to_element(MODAL_CLOSE)

    @allure.step('Ввести адрес электронной почты в поле Email')
    def input_email(self):
        self.input_text(EMAIL, 'petergaas8126@yandex.ru')

    @allure.step('Ввести пароль в поле Пароль')
    def input_password(self):
        self.input_text(PASSWORD, '123456')

    @allure.step('Нажать на кнопку Войти')
    def click_button_enter(self):
        self.click_to_element(BUTTON_ENTER)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_button_place_order(self):
        self.click_to_element(BUTTON_PLACE_ORDER)
