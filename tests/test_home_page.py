import allure
from data_static import ORDER_FEED_URL, LOGIN_URL, MAIN_URL
from locators.home_page_locators import INGREDIENT_DETAIL, INGREDIENT, TEXT_ORDER, BUTTON_PLACE_ORDER
from pages.home_page import HomePage


class TestHomePage:
    @allure.title('Переход в Ленту заказов')
    @allure.description('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self, chrome_driver):
        home_page = HomePage(chrome_driver)
        home_page.click_to_order_feed()

        assert home_page.get_current_url() == ORDER_FEED_URL

    @allure.title('Посмотреть детали описание ингредиента')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_show_detail(self, chrome_driver):
        home_page = HomePage(chrome_driver)
        home_page.wait_element_to_be_clickable(INGREDIENT)
        home_page.click_to_ingredient()

        assert home_page.get_text_from_element(INGREDIENT_DETAIL) == 'Детали ингредиента'

    @allure.title('Закрыть детали описание ингредиента')
    @allure.description('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_detail_click_to_cross(self, chrome_driver):
        home_page = HomePage(chrome_driver)
        home_page.wait_element_to_be_clickable(INGREDIENT)
        home_page.click_to_ingredient()
        home_page.click_to_close_modal_ingredient_detail()

        assert home_page.wait_element_to_be_clickable(INGREDIENT_DETAIL) is None

    @allure.title('Оформить заказ от авторизованного пользователя')
    @allure.description('Залогиненный пользователь может оформить заказ.')
    def test_login_user_can_create_order(self, chrome_driver):
        home_page = HomePage(chrome_driver)
        home_page.click_to_personal_account()
        home_page.wait_url_contains(LOGIN_URL)
        home_page.input_email()
        home_page.input_password()
        home_page.click_button_enter()
        home_page.wait_url_contains(MAIN_URL)
        home_page.wait_element_to_be_clickable(BUTTON_PLACE_ORDER)
        home_page.click_button_place_order()

        assert home_page.get_text_from_element(TEXT_ORDER) == 'Ваш заказ начали готовить'

