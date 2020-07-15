from behave import *
import time

from selenium.common.exceptions import NoSuchElementException

use_step_matcher('re')

@when("I checked menu's names")
def step_impl(context):
    text1 = context.browser.find_element_by_xpath('//*[@id="menu-6474"]/li[2]/a')


@then('I check number of complaints')
def step_impl(context):
    try:
        text1 = context.browser.find_element_by_xpath('//*[@id="panel-4"]/div[2]/div/div[2]/div/div/div[1]/a[2]/span[1]/span')
    except NoSuchElementException:
        print('FAIL')

@then('I check arenda word')
def step_impl(context):
    title_xpath = context.browser.find_element_by_xpath("//*[contains(text(), 'Rent')]")
    assert title_xpath.is_displayed()