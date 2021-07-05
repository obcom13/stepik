from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_id("book")
button.click()
element2 = browser.find_element_by_id("input_value")
x = element2.text
y = calc(x)
element3 = browser.find_element_by_id("answer")
element3.send_keys(y)
element4 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
element4.click()
