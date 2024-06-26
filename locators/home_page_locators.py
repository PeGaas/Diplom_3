from selenium.webdriver.common.by import By

# Личный кабинет
PERSONAL_ACCOUNT = [By.XPATH, "//p[.='Личный Кабинет']"]

# Лента заказов
ORDER_FEED = [By.XPATH, "//p[.='Лента Заказов']"]

# Ингридиент
INGREDIENT = [By.XPATH, "//a[.='0988Флюоресцентная булка R2-D3']"]

# Детали ингридиента
INGREDIENT_DETAIL = [By.CSS_SELECTOR, ".Modal_modal__title_modified__3Hjkd"]

# Крестик для закрытия детального просмотра ингридиента
MODAL_CLOSE = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]

# Кнопка оформить заказ
BUTTON_PLACE_ORDER = [By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"]

# Текс Ваш заказ начали готовить
TEXT_ORDER = [By.CSS_SELECTOR, ".text_type_main-small"]

