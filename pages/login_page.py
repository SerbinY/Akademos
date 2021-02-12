from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def user_should_see_welcome_text_after_login(self):
        self.browser.find_element(*LoginPageLocators.INPUT_USER_NAME).send_keys('Serbin')
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys('123456')
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        wellcome_text = self.browser.find_element(*LoginPageLocators.WELLCOME_TEXT).text
        assert 'Hello, Serbin' in wellcome_text, 'Wellcome text is not displaed'




