import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    #wd = webdriver.Chrome()
    #wd = webdriver.Firefox(capabilities={"marionette": False})
    wd = webdriver.Firefox(firefox_binary="c:\\Users\\Bekhzod\\AppData\\Local\\Firefox Nightly\\firefox.exe")
    #wd = webdriver.Firefox()
    #wd = webdriver.Edge()
    #wd = webdriver.Ie()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver\n")
    #driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Google Search"))
    #driver.quit()