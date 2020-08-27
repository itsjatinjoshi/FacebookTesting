from selenium.webdriver.common.by import By

from Pages.UserProfilePage import UserProfilePage


class FacebookHomePage:

    def __init__(self, driver):
        self.driver = driver

    home_icon = (By.CSS_SELECTOR, "a[aria-label='Home']")
    user_profile_link = (By.CSS_SELECTOR, "a[aria-label='Jatinn']")

    def get_home_link(self):
        return self.driver.find_element(*FacebookHomePage.home_icon)

    def get_profile_link(self):
        self.driver.find_element(*FacebookHomePage.user_profile_link).click()
        user_profile = UserProfilePage(self.driver)
        return user_profile
