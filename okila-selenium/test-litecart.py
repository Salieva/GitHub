import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    #wd = webdriver.Chrome()
    #wd = webdriver.Ie()
    #wd = webdriver.Firefox(firefox_binary="c:\\program files\\Firefox Nightly\\firefox.exe")
    #wd = webdriver.Firefox(capabilities={"marionette": False})
    #wd = webdriver.Firefox(firefox_binary="c:\\program files\\Mozilla Firefox\\firefox.exe")
    #wd = webdriver.Edge()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.delete_all_cookies()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    #driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar")))