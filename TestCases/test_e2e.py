import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.HomePage import FacebookHomePage
from Pages.LoginPage import Login
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self):
        login_page = Login(self.driver)

        login_page.get_forget_password().click()
        login_page.select_cancel_password().click()

        login_page.get_user_email()
        login_page.get_user_password()
        # login_page.get_login_button()

        fb_home_page = login_page.get_login_button()
        fb_home_page.get_home_link().click()
        # self.driver.implicitly_wait(10)
        time.sleep(10)

        fb_user_profile_page = fb_home_page.get_profile_link()
        # self.driver.implicitly_wait(10)
        # time.sleep(10)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(fb_user_profile_page.photos))

        fb_user_profile_page.get_photos().click()
        time.sleep(5)

        fb_user_profile_page.get_photos_of_you().click()

        account_logout = fb_user_profile_page.get_all_photos()
        account_logout.get_account_link().click()
        account_logout.get_logout_link().click()
        time.sleep(10)
