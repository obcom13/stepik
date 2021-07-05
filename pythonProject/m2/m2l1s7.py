import math
import time
from selenium import webdriver
link = "http://suninjuly.github.io/get_attribute.html"
try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
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