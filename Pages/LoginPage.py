from selenium.webdriver.common.by import By

from Pages.HomePage import FacebookHomePage


class Login:
    user_email = (By.CSS_SELECTOR, "input[name='email'")
    user_password = (By.CSS_SELECTOR, "input[placeholder='Password']")
    login_button = (By.CSS_SELECTOR, "button[name='login']")
    forget_password = (By.LINK_TEXT, "Forgot account?")
    cancel_login = (By.CSS_SELECTOR, "span[class='uiButtonText']")

    def __init__(self, driver):
        self.driver = driver

    def get_forget_password(self):
        return self.driver.find_element(*Login.forget_password)

    def select_cancel_password(self):
        return self.driver.find_element(*Login.cancel_login)

    def get_user_email(self):
        # please either hardcore your username in send_keys brackets or enter
        username = input("username: ")
        return self.driver.find_element(*Login.user_email).send_keys(username)

    def get_user_password(self):
        # please either hardcore your password in send_keys brackets or enter
        password = input("username: ")
        return self.driver.find_element(*Login.user_password).send_keys(password)

    def get_login_button(self):
        self.driver.find_element(*Login.login_button).click()
        fb_home_page = FacebookHomePage(self.driver)
        return fb_home_page

        # self.driver.find_element_by_css_selector("input[name='email']")
        # self.driver.find_element_by_css_selector("input[placeholder='Password']")
        # self.driver.find_element_by_css_selector("button[name='login']").click()
