from selenium.webdriver.common.by import By



class LoginPageLocators():
    INPUT_USER_NAME = (By.CSS_SELECTOR, '#login-form [name="username"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#login-form [name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-form [value="Login"]')
    WELLCOME_TEXT = (By.CSS_SELECTOR, '#logged-in h1')

