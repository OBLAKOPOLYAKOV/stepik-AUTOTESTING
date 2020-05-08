import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
from selenium import webdriver
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('url', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])#if u need more url, just do it
def test_button_add_in_bascet(browser, url):
    browser.get(f"{url}")
    button=browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, 'button does not exist'