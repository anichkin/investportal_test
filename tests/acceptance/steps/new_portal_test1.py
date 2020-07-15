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
    link = context.browser.find_element(By.XPATH, '//*[@id="second-navbar"]/ul/li[1]/a')
    action = ActionChains(context.browser)
    action.move_to_element(link)
    link2 = context.browser.find_element(By.XPATH, '//*[@id="tab-1"]/div/div[2]/ul/li[1]/a')
    action.move_to_element(link2)
    link3 = context.browser.find_element(By.XPATH, '//*[@id="tab1-inner-1"]/div/ul[1]/li[1]/a')
    action.move_to_element(link3).click().perform()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[2]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[3]/a').click()

    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[4]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[5]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[6]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[7]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[8]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="myScrollspy"]/ul/li[8]/a').click()


