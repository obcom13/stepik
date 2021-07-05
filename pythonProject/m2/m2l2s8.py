import time
import os
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_name("firstname")
    element1.send_keys('Name')
    element2 = browser.find_element_by_name("lastname")
    element2.send_keys('Surname')
    element3 = browser.find_element_by_name("email")
    element3.send_keys('box@mail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element4 = browser.find_element_by_name("file")
    element4.send_keys(file_path)
    element5 = browser.find_element_by_css_selector(".btn-primary")
    element5.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла