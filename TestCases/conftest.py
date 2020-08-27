import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default='chrome')


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=option,
                                  executable_path="C:\\Users\Jatin-PC\Desktop\Drivers\chromedriver_win32\chromedriver.exe")
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:\\Users\Jatin-PC\Desktop\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")
    elif browser_name == 'IE':
        # driver = webdriver.Ie(
        #     executable_path="C:\\Users\Jatin-PC\Desktop\Drivers\IEDriverServer_x64_2.53.1\IEDriverServer.exe")
        pass
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.quit()
# todo: will run this test later, not working, take time

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# languages = driver.find_elements_by_xpath(
#     "//ul[@class='uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']/li/a")
#
# print("Break Point 1")
# lang_list = ['English (US)']
# print("Break Point 2", lang_list)
# for language in languages:
#     lang_list.append(language.get_attribute("href"))
#
# for link in lang_list:
#     if driver.find_element_by_xpath("//ul[@class='uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']/li/a[@href=%s]" % link) == 'https://www.facebook.com/':
#         pass
#     else:
#         driver.find_element_by_xpath("//ul[@class='uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']/li/a[@href=%s]" % link).click()
#
#     time.sleep(4)


# # str(language)
# print("Language: ", language.get_attribute("href"))
# # print(str(language.text))
# if language == any(lang_list):
#     print("inside the list: ", language.text)
#     pass
# else:
#
#     print("ELSE LIST: ", lang_list)
#     language.click()
#     time.sleep(3)
#     # languages = driver.find_elements_by_xpath(
#     #     "//ul[@class='uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']/li/a")
