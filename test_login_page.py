from pages.login_page import LoginPage



def test_login_page(browser):
    link = "http://qa.odessa.akademos.com/qa.php"
    page = LoginPage (browser,link)
    page.open()
    page.user_should_see_welcome_text_after_login()



