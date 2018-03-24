import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color

@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    # wd = webdriver.Edge()
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla Firefox\\firefox.exe")
    # print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False

def test_example(driver):
    # driver.get("http://localhost/litecart/admin/")
    # driver.delete_all_cookies()
    driver.get("http://localhost/litecart/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "box-campaigns")))

    box = driver.find_element_by_id("box-campaigns")
    pr_reg_price = box.find_element_by_css_selector("s.regular-price").text
    pr_camp_price = box.find_element_by_css_selector("strong.campaign-price").text
    pr_name = box.find_element_by_css_selector(".name").text
# тестируем зачеркнутость регулярной цены
    assert is_element_present(box, By.CSS_SELECTOR, 's.regular-price') is True
# тестируем наличие жирного шрифта в акционной цене
    assert is_element_present(box, By.CSS_SELECTOR, 'strong.campaign-price') is True
# тестируем размер шрифта регулярной цены
    pr_reg_font_size = box.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size')
# тестируем размер шрифта акционной цены
    pr_camp_font_size = box.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size')
# сравниваем размеры регулярной и акционной цен
    assert float(pr_camp_font_size[:-2]) > float(pr_reg_font_size[:-2])

    pr_reg_color = box.find_element_by_css_selector('s.regular-price').value_of_css_property('color')
    pr_reg_color = Color.from_string(pr_reg_color).hex
    assert pr_reg_color[1:3] == pr_reg_color[3:5] == pr_reg_color[5:]

    pr_camp_color = box.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')
    pr_camp_color = Color.from_string(pr_camp_color).hex
    assert pr_camp_color[3:5] == '00'
    assert pr_camp_color[5:] == '00'




