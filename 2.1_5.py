from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    otvet=browser.find_element_by_css_selector(".form-control")
    otvet.send_keys(y)
    iamrobot=browser.find_element_by_css_selector("#robotCheckbox")
    iamrobot.click()
    peoplenotrules=browser.find_element_by_css_selector("#peopleRule")
    peoplenotrules.click()
    robotrules=browser.find_element_by_css_selector("#robotsRule")
    robotrules.click()
    button=browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()