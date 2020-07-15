from behave import *
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher('re')

@When('I go to the one trade page')
def step_impl(context):
    time.sleep(6)
    context.browser.find_element(By.XPATH, '//*[@id="tenderDetailsAll"]/div[1]/div/div/div[2]/div/div/div[3]/div[2]/span/a').click()
    time.sleep(6)

@When('I download the document')
def step_impl(context):
    context.browser.switch_to_window(context.browser.window_handles[1])
    context.browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/ul/li[4]/a').click()
    time.sleep(3)
    title_xpath = WebDriverWait(context.browser, 5).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@id="attachedFiles"]/div/div/table/tbody/tr[1]/td[1]/a'))
    )
    title_xpath.click()
    context.browser.find_element(By.XPATH, '//*[@id="mobile-menu"]/ul/li[2]/a').click()
    context.browser.find_element(By.XPATH, '//*[@id="tenderCalendarTab"]/strong').click()
    calendar = WebDriverWait(context.browser, 5).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@id="tenderCalendarWrapper"]/div[1]/div[2]'))
    )
    calendar.click()
    context.browser.find_element(By.XPATH, '//*[@id="logo"]').click()
    time.sleep(3)