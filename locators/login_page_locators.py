from selenium.webdriver.common.by import By

# Личный кабинет
RECOVER_PASSWORD = [By.XPATH, "//a[.='Восстановить пароль']"]

# Поле Email
EMAIL = [By.NAME, 'name']

# Поле Пароль
PASSWORD = [By.NAME, 'Пароль']

# Кнопка Войти
BUTTON_ENTER = [By.CSS_SELECTOR, '.button_button__33qZ0']

# История заказов
ORDER_HISTORY = [By.XPATH, '//a[.="История заказов"]']

# Выход из аккаунта
EXIT_ACCOUNT = [By.CSS_SELECTOR, '.Account_button__14Yp3']


