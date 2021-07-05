from selenium import webdriver
link = "https://www.google.com/"
browser = webdriver.Chrome()
browser.get(link)
element = browser.find_element_by_name("btnK")
element.get_attribute()