from selenium import webdriver
import time
import math
import os
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser=webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(".btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x=browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_css_selector("#answer").send_keys(calc(x))
    browser.find_element_by_css_selector(".btn").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    browser.quit()