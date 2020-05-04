from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    s=int(x)+int(y)
    select=Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(s))
    browser.find_element_by_css_selector("button.btn").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)