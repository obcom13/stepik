import math
import time
from selenium import webdriver
link = "http://suninjuly.github.io/math.html"
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)
    element1 = browser.find_element_by_id("robotCheckbox")
    element1.click()
    element2 = browser.find_element_by_id("robotsRule")
    element2.click()
    element3 = browser.find_element_by_css_selector(".btn.btn-default")
    element3.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла