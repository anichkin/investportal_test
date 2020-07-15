import selenium
from behave import *
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher('re')

@Then('I check tender part')
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="master-content"]/div[2]/div[1]/div[1]/a/div/div/img').click()
    context.browser.find_element(By.XPATH, '//*[@id="master-content"]/div[2]/div[2]/div/ul/li[2]/a/span').click()
    context.browser.find_element(By.XPATH, '//*[@id="filterTab"]/div[1]/div[2]/a').click()
    time.sleep(3)
    context.browser.find_element(By.XPATH, '//*[@id="tenderKind5"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="moreFilters"]/div[6]/div/div/div/div[2]/a').click()
    time.sleep(3)
    element = context.browser.find_element_by_xpath('//*[@id="moreFiltersLink"]')  # you can use ANY way to locate element
    coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
    context.browser.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))
    context.browser.find_element(By.XPATH, '//*[@id="moreFiltersLink"]').click()
    context.browser.find_element(By.XPATH, '//*[@id="moreFilters"]/div[6]/div/div/div/div[3]/a').click()
    context.browser.find_element_by_xpath('//*[@id="FilterName"]').send_keys('test_filter')
    context.browser.find_element_by_xpath('//*[@id="AddSearchTracking"]/div[1]/div[2]/div/button').click()
    context.browser.find_element_by_xpath('//*[@id="inner"]/div[6]/div/div/a').click()
    time.sleep(3)
    account_xpath = WebDriverWait(context.browser, 5).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@id="sticky-wrapper"]/header/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/a/div/div/span'))
    )
    account_xpath.click()
    context.browser.find_element(By.XPATH, '//*[@id="master-content"]/div[2]/div[1]/div[1]/a/div/div/img').click()
    context.browser.find_element(By.XPATH, '//*[@id="master-content"]/div[2]/div[2]/div/ul/li[2]/a/span').click()
    context.browser.find_element_by_xpath("//*[contains(text(), 'test_filter')]")
    context.browser.find_element_by_xpath('//*[@id="filterTab"]/div[2]/div[1]/div[2]/div[2]/a/img').click()
    context.browser.switch_to.alert.accept()
    context.browser.find_element_by_xpath('//*[@id="master-content"]/div[2]/div[1]/nav/ul/li[1]/a/img[2]').click()
    context.browser.find_element_by_xpath('//*[@id="master-content"]/div[2]/div[2]/div/ul/li[2]/a/span').click()
    context.browser.find_element_by_xpath('//*[@id="mobile-menu"]/ul/li[2]/a/div').click()
    context.browser.find_element_by_xpath('//*[@id="tendersMainWrapper"]/div[1]/div[1]/div/div[1]/button').click()
    context.browser.find_element_by_xpath('//*[@id="sticky-wrapper"]/header/div[3]/div/div/div[2]/div/div/div[1]/div/div[4]/a/div/div/span').click()
    context.browser.find_element_by_xpath('//*[@id="master-content"]/div[2]/div[1]/div[1]/a/div/p[1]').click()
    context.browser.find_element_by_xpath('//*[@id="favTab"]/div[2]/div[1]/div[1]/span/span').click()
    context.browser.find_element_by_xpath('//*[@id="master-content"]/div[2]/div[1]/nav/ul/li[1]/a/img[2]').click()
    time.sleep(3)

@Then('I check complain part')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="master-content"]/div[2]/div[1]/div[3]/a/div/div/img').click()
    context.browser.find_element_by_xpath('//*[@id="master-content"]/div[2]/div[2]/div[1]/div[2]/a').click()
    context.browser.find_element_by_xpath('//*[@id="directAppealForm"]/div/div[1]/fieldset[1]/div[5]/div/label/span').click()
    context.browser.find_element_by_xpath('//*[@id="Appeal_OrgType"]').send_keys('sphere of acivity')
    select = Select(context.browser.find_element_by_xpath('//*[@id="Appeal_ProblemTypeId"]'))
    select.select_by_value('4317')
    context.browser.find_element_by_xpath('//*[@id="Appeal_Message"]').send_keys('Amy normally hated Monday mornings,'
                                                                                 ' but this'
                                                                                 ' year was different. '
                                                                                 'Kamal was in her art class and she '
                                                                                 'liked Kamal. She was waiting'
                                                                                 ' outside the classroom when her'
                                                                                 ' friend Tara arrived.')
    context.browser.find_element_by_xpath('//*[@id="CaptchaText"]').send_keys('7654675875876587568568')
    time.sleep(2)
    context.browser.find_element_by_xpath('//*[@id="directAppealForm"]/div/div[2]/div/div[2]/div[6]/div[2]/div[2]/button').click()
    context.browser.find_element_by_xpath('//*[@id="logo"]/img').click()