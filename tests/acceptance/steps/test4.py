import time

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver

use_step_matcher('re')

@when ('I go to active investor page')
def step_imp(context):
    link = context.browser.find_element(By.XPATH, '//*[@id="big-menu-href"]/span[1]')
    link.click()
    time.sleep(10)
    link2 = context.browser.find_element(By.XPATH, '//*[@id="menu-6484"]/li[6]')
    link2.click()
    link3 = context.browser.find_element(By.XPATH, '//*[@id="objectChoose"]/span')
    link3.click()

    s = Select(context.browser.find_element(By.CLASS_NAME, 'btn dropdown-toggle selectpicker btn-default'))
    word = 'Здание'
    good_word = word.encode('cp1251').decode('utf8')
    s.select_by_title(good_word)
    time.sleep(100)
