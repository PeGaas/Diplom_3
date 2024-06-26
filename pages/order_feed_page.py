import time
import allure
from locators.home_page_locators import PERSONAL_ACCOUNT, ORDER_FEED, INGREDIENT, MODAL_CLOSE, BUTTON_PLACE_ORDER
from locators.login_page_locators import EMAIL, PASSWORD, BUTTON_ENTER
from locators.order_feed_page_locators import ORDER
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать на История заказов')
    def click_to_order_feed(self):
        self.click_to_element(ORDER_FEED)

    @allure.step('Нажать на заказ')
    def click_to_order(self):
        self.click_to_element(ORDER)

    @allure.step('Ожидать появления заказа в работе')
    def wait_number_order_in_work(self):
        time.sleep(3)

