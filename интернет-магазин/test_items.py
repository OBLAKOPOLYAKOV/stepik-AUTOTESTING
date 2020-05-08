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
@pytest.mark.parametrize('url', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_answer1(browser, url):
    link=f"{url}"
    browser.get(link)
    time.sleep(30)