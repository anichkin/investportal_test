from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

use_step_matcher('re')

@when('I click on the some buttons')
def step_imp(context):
    link = context.browser.find_element(By.XPATH, '//*[@id="header-topic-slider"]/div/div/div[1]/span').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="header-topic-slider"]/div/div/div[2]/span').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="header-topic-slider"]/div/div/div[3]/span').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="header-topic-slider"]/div/div/div[4]/span').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="header-topic-slider"]/div/div/div[5]/span').click()



