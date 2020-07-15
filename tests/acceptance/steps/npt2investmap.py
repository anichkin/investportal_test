from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher('re')

@when('I go to new investmap')
def step_imp(context):
    link = context.browser.find_element(By.XPATH, '//*[@id="second-navbar"]/ul/li[1]/a')
    action = ActionChains(context.browser)
    action.move_to_element(link)
    link2 = context.browser.find_element(By.XPATH, '//*[@id="tab-1"]/div/div[2]/ul/li[2]/a')
    action.move_to_element(link2).click().perform()
    element = WebDriverWait(context.browser, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[1]'))
    )
    link = context.browser.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[2]/div[1]').click()
    element = WebDriverWait(context.browser, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#wrapper > div.search-wrapper > div.filter-wrap-list.js-act > ul > li:nth-child(2) > a'))
    )
    time.sleep(10)
    link = context.browser.find_element(By.CSS_SELECTOR, '#wrapper > div.search-wrapper > div.filter-wrap-list.js-act > ul > li:nth-child(2) > a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="filter-btn"]').click()
    time.sleep(10)

