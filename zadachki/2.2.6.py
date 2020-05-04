from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value").text
    y=calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("input[type=checkbox]").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element_by_css_selector("#robotsRule"))
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)