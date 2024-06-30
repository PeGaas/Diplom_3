import allure
from locators.order_feed_page_locators import MODAL_ORDER_DETAIL, ORDER, ORDERS_ALL_TIME, COMPLETE_TODAY, ORDER_IN_WORK
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('Открыть детали заказа')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_show_order_detail(self, chrome_driver):
        order_feed_page = OrderFeedPage(chrome_driver)
        order_feed_page.click_to_order_feed()
        order_feed_page.wait_element_to_be_clickable(ORDER)
        order_feed_page.click_to_order()
        order_feed_page.element_to_be_present_in_page(MODAL_ORDER_DETAIL)

        assert str(order_feed_page.get_text_from_element(MODAL_ORDER_DETAIL)).find('Состав')

    @allure.title('Проверить что заказ пользователя есть в ленте заказов')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_from_order_history_show_on_order_feed(self, chrome_driver, api_create_order_authorized_user):
        order_number = api_create_order_authorized_user.json()['order']['number']
        order_feed_page = OrderFeedPage(chrome_driver)
        order_feed_page.click_to_order_feed()
        order_feed_page.wait_element_to_be_clickable(ORDER)
        order_feed_page.click_to_order()
        order_feed_page.element_to_be_present_in_page(MODAL_ORDER_DETAIL)
        str_order = str(order_feed_page.get_text_from_element(MODAL_ORDER_DETAIL))
        str_order = str_order[0:8]
        str_order = ''.join(char for char in str_order if char.isalnum())

        assert str('#' + str_order) == '#0' + str(order_number)

    @allure.title('Счетчик всех заказов увеличивается после создания заказа')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_order_counter_is_completed_all_time_increases(self, chrome_driver, api_create_order_authorized_user,
                                                                  api_get_orders_user):
        total = api_get_orders_user.json()['total']
        order_feed_page = OrderFeedPage(chrome_driver)
        order_feed_page.click_to_order_feed()
        order_feed_page.element_to_be_present_in_page(ORDERS_ALL_TIME)
        number_total = order_feed_page.get_text_from_element(ORDERS_ALL_TIME)

        assert int(number_total) == total

    @allure.title('Счетчик дневных заказов увеличивается после создания заказа')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_order_counter_today_increases(self, chrome_driver, api_create_order_authorized_user,
                                                  api_get_orders_user):
        total_today = api_get_orders_user.json()['totalToday']
        order_feed_page = OrderFeedPage(chrome_driver)
        order_feed_page.click_to_order_feed()
        order_feed_page.element_to_be_present_in_page(COMPLETE_TODAY)
        number_total_today = order_feed_page.get_text_from_element(COMPLETE_TODAY)

        assert int(number_total_today) == total_today

    @allure.title('Новый заказ сразу попадает в раздел "В работе"')
    @allure.description('После оформления заказа его номер появляется в разделе "В работе"')
    def test_create_order_number_appears_in_progress_section(self, chrome_driver, api_create_order_authorized_user,
                                                             api_get_orders_user):
        create_order = api_create_order_authorized_user.json()['order']['number']
        order_feed_page = OrderFeedPage(chrome_driver)
        order_feed_page.click_to_order_feed()
        order_feed_page.element_to_be_present_in_page(ORDER_IN_WORK)
        order_feed_page.wait_number_order_in_work('class', 'text text_type_digits-default mb-2')
        order_in_work = order_feed_page.get_text_from_element(ORDER_IN_WORK)

        assert int(create_order) == int(order_in_work)
