from selenium.webdriver.common.by import By

# Личный кабинет
PERSONAL_ACCOUNT = [By.XPATH, '//p[.="Личный Кабинет"]']

# Поле email
EMAIL = [By.NAME, 'name']

# Кнопка Восстановить
BUTTON_RECOVER = [By.CSS_SELECTOR, '.button_button__33qZ0']

# Поле Пароль
PASSWORD = [By.NAME, 'Введите новый пароль']

# Показать пароль
SHOW_PASSWORD = [By.CSS_SELECTOR, '.input__icon']

# Class Active
CLASS_ACTIVE = [By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]']

