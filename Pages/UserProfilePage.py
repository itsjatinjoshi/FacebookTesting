from selenium.webdriver.common.by import By

from Pages.LogoutPage import ProfileLogout


class UserProfilePage:

    def __init__(self, driver):
        self.driver = driver

    # photos = (By.XPATH, "//div[@class='bp9cbjyn j83agx80 btwxx1t3 k4urcfbm']/a[4]/div/span")
    photos = (By.XPATH,
              "//div[@class='rq0escxv lpgh02oy du4w35lb rek2kq2y']//div[@class='bp9cbjyn j83agx80 btwxx1t3 k4urcfbm']/a[4]/div/span")
    photos_of_you = (By.XPATH, "//span[contains(text(),'Photos of You')]")
    all_photos = (By.XPATH, "//div[@class='lyjsgrqv']/a")

    def get_photos(self):
        return self.driver.find_element(*UserProfilePage.photos)

    def get_photos_of_you(self):
        return self.driver.find_element(*UserProfilePage.photos_of_you)

    def get_all_photos(self):
        photos = self.driver.find_elements(*UserProfilePage.all_photos)
        print(photos)
        for photo in photos:
            pics = photo.get_attribute('href')
            print(pics)

        account = ProfileLogout(self.driver)
        return account
