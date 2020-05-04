from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("img#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    otvet=browser.find_element_by_css_selector("#answer")
    otvet.send_keys(y)
    iamrobot=browser.find_element_by_css_selector("#robotCheckbox")
    iamrobot.click()
    robotrules=browser.find_element_by_css_selector("#robotsRule")
    robotrules.click()
    button=browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()