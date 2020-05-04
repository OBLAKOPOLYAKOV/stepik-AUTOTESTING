from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector("[name=firstname]")
    name.send_keys("MIKHAIL")
    lastname = browser.find_element_by_css_selector("[name=lastname]")
    lastname.send_keys("POLYAKOV")
    mail = browser.find_element_by_css_selector("[name=email")
    mail.send_keys("mail@mail.com")
    element = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    browser.find_element_by_css_selector(".btn").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()