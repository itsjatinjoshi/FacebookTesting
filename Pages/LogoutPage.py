from selenium.webdriver.common.by import By


class ProfileLogout:

    def __init__(self, driver):
        self.driver = driver

    account_icon = (By.CSS_SELECTOR, 'div[aria-label="Account"]')
    logout_link = (By.XPATH, "//span[contains(text(),'Log Out')]")
    # logout = (By.CSS_SELECTOR, "")

    def get_account_link(self):
        return self.driver.find_element(*ProfileLogout.account_icon)

    def get_logout_link(self):
        return self.driver.find_element(*ProfileLogout.logout_link)
