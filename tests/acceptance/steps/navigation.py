from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome('/webdrivers/chromedriver')
    context.browser.set_window_size(1700, 1300)
    context.browser.get('https://investmoscow.ru/')

@given('I am on the new homepage')
def step_impl(context):
    context.browser = webdriver.Chrome('/webdrivers/chromedriver')
    context.browser.set_window_size(1700, 1300)
    context.browser.get('http://new.investmoscow.upt24.ru/')

@given('I am on the new rc homepage')
def step_impl(context):
    context.browser = webdriver.Chrome('/webdrivers/chromedriver')
    context.browser.set_window_size(1700, 1300)
    context.browser.get('http://rc.investmoscow.ru/')

@given('I am on the engtenders page')
def step_impl(context):
    context.browser = webdriver.Chrome('/webdrivers/chromedriver')
    context.browser.set_window_size(1700, 1300)
    context.browser.get('http://en.investmoscow.ru/tenders')

@given('I am on the tenders page')
def step_impl(context):
    context.browser = webdriver.Chrome('/webdrivers/chromedriver')
    context.browser.set_window_size(1700, 1300)
    context.browser.get('http://investmoscow.ru/tenders')


@then('I am on the tenders page')
def step_impl(context):
    expected_url = 'https://investmoscow.ru/tenders'
    assert context.browser.current_url == expected_url


@then('I am on the registration page')
def step_impl(context):
    second_name_xpath = context.browser.find_element_by_xpath('//*[@id="master-content"]/div[3]/div/div/form/div[2]/div[1]/div/div[1]/div[1]/label')
    assert second_name_xpath.is_displayed()


@then('I am on the account page')
def step_impl(context):
    check = context.browser.find_element_by_xpath('// *[ @ id = "content-header"]')

