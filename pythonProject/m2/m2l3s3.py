from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/alert_accept.html"
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element_by_class_name("btn-primary")
    element1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element2 = browser.find_element_by_id("input_value")
    x = element2.text
    y = calc(x)
    element3 = browser.find_element_by_id("answer")
    element3.send_keys(y)
    element4 = browser.find_element_by_class_name("btn-primary")
    element4.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
