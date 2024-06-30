from selenium.webdriver.common.by import By

# Заказ
ORDER = [By.XPATH, "//li[contains(@class, 'OrderHistory_list')]"]

# Окно с деталями о заказе
MODAL_ORDER_DETAIL = [By.CSS_SELECTOR, ".Modal_orderBox__1xWdi"]

# Выполнено за все время
ORDERS_ALL_TIME = [By.XPATH, "//p[contains(@class, 'OrderFeed_number')]"]

# Выполнено за сегодня
COMPLETE_TODAY = [By.CSS_SELECTOR, "div:nth-of-type(3) > .OrderFeed_number__2MbrQ"]

# Заказ в работа
ORDER_IN_WORK = [By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem > .text"]
