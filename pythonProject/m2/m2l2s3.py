import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_id("num1")
    num1 = element1.text
    print(num1)
    element2 = browser.find_element_by_id("num2")
    num2 = element2.text
    print(num2)
    result = int(num1) + int(num2)
    print(result)
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_visible_text(str(result))
    element3 = browser.find_element_by_css_selector(".btn.btn-default")
    element3.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла