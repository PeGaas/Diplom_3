import allure
from locators.home_page_locators import ORDER_FEED

from locators.order_feed_page_locators import ORDER, ORDER_IN_WORK
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
    def wait_number_order_in_work(self, attribute, class_name):
        self.text_to_be_present_in_element_attribute(ORDER_IN_WORK, attribute, class_name)

