from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
link = "https://vk.com/im?sel=151945668"
import os
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("#email").send_keys("89197629472")
    browser.find_element_by_css_selector("#pass").send_keys("Kraze10375")
    browser.find_element_by_css_selector("#login_button").click()
    time.sleep(3)
    browser.find_element_by_css_selector(".im_editable").send_keys("ПРИВЕТ,ЭТО РОБОТ ПИШЕТ, файл не открывай ни в коем случае)))00")
    browser.execute_script("return arguments[0].scrollIntoView(true);",browser.find_element_by_css_selector(".im-send-btn._im_send"))
    browser.find_element_by_css_selector(".im-send-btn._im_send").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()