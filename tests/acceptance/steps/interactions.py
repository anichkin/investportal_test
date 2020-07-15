import time

from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

use_step_matcher('re')


@when('I click on the tenders link')
def step_impl(context):
    link = context.browser.find_element_by_xpath('//*[@id="bidding"]/div[1]/h2/a')
    link.click()


@when('I click on the menu button')
def step_impl(context):
    link = context.browser.find_element_by_id('big-menu-href')
    link.click()



@when('I go to the online services')
def step_impl(context):
    link = context.browser.find_element_by_css_selector('#sticky-wrapper > div > ul > li:nth-child(4) > a')
    link.click()



@when('I click on the search button')
def step_impl(context):
    link = context.browser.find_element_by_xpath('//*[@id="mainFilterSelectors"]/div/div[4]/button')
    link.click()


@when('I click on the account button')
def step_impl(context):
    link = context.browser.find_element_by_xpath('//*[@id="sticky-wrapper"]/div/div/div/div[2]/div/div/div[2]/div/div[4]/div/div[1]/a/div/div[2]/span')
    link.click()


@when('I click on the registration button')
def step_impl(context):
    link = context.browser.find_element_by_xpath('//*[@id="master-content"]/div[3]/div/div/form/div/div/div[4]/div[2]/a')
    link.click()


@when('Scroll frame window')
def step_impl(context):
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'fancybox-iframe'))
    )
    context.browser.switch_to.frame(context.browser.find_element(By.CLASS_NAME, 'fancybox-iframe'))
    context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")



@when('I click on the agreement button')
def step_impl(context):
    link = context.browser.find_element_by_xpath('//*[@id="Agree"]')
    link.click()


@when('I wrote credits in form')
def step_impl(context):
    form = context.browser.find_element_by_xpath('// *[ @ id = "Login"]')
    form.send_keys('anichkin@upt24.ru')
    form2 = context.browser.find_element_by_xpath('//*[@id="Password"]')
    form2.send_keys('1234567')

@when('I click to enter')
def step_impl(context):
    link = context.browser.find_element_by_xpath('//*[@id="master-content"]/div[3]/div/div/form/div/div/div[4]/div[1]/input')
    link.click()

@given('Authorization in dgp')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://dgp.investmoscow.upt24.ru/')
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="LoginTextBox"]'))
    )
    form = context.browser.find_element_by_xpath('//*[@id="LoginTextBox"]')
    form.send_keys('login')
    form2 = context.browser.find_element_by_xpath('//*[@id="PasswordTextBox"]')
    form2.send_keys('pswrd')
    link = context.browser.find_element_by_xpath('//*[@id="LoginForm"]/fieldset/div[4]/div/button')
    link.click()


@when('I click on "create project" button')
def step_impl(context):
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="tree-panel"]/table/tbody/tr[1]/td/div/div[1]/ul/li/div/a'))
    )
    link = context.browser.find_element_by_xpath('//*[@id="tree-panel"]/table/tbody/tr[1]/td/div/div[1]/ul/li/div/a')
    link.click()

@when('I fill the forms')
def step_impl(context):
    s1 = Select(context.browser.find_element(By.ID, 'objType'))
    s1.select_by_value('819')
    form = context.browser.find_element_by_xpath('//*[@id="ucSelectAddress_tbGeneralAddress"]')
    form.click()
    word = 'про'
    good_word = word.encode('cp1251').decode('utf8')
    form.send_keys(good_word)
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="addressucSelectAddress"]/table/tbody/tr[1]/td[2]/ul/li[4]'))
    )
    element.click()
    form2 = context.browser.find_element_by_xpath('//*[@id="tbRoomPlace"]')
    word2 = 'Расположение помещения тест'
    good_word2 = word2.encode('cp1251').decode('utf8')
    form2.send_keys(good_word2)
    form3 = context.browser.find_element_by_xpath('//*[@id="tbRoomSquare"]')
    word3 = '32'
    form3.send_keys(word3)
    button = context.browser.find_element_by_xpath('//*[@id="form1"]/div[4]/div/div/div[6]/fieldset/div[1]/div/div/div/div/a[2]/i')
    button.click()
    button.click()
    time.sleep(10)
    context.browser.find_element_by_xpath('//*[@id="70876"]').click()
    context.browser.find_element_by_xpath('//*[@id="bSelect"]').click()

    s2 = Select(context.browser.find_element(By.ID, 'selTarget'))
    s2.select_by_value('37005')

    s3 = Select(context.browser.find_element(By.ID, 'selMechanism'))
    s3.select_by_value('511')
    context.browser.find_element_by_xpath('//*[@id="btnSaveButton"]').click()

    element2 = WebDriverWait(context.browser, 100).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="form1"]/div[4]/div/div[3]/span'))
    )
    element2.click()
    context.browser.find_element_by_xpath('//*[@id="DeleteButton"]').click()
    context.browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[1]').click()
    element3 = WebDriverWait(context.browser, 100).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="lblHeaderTitle"]/ul/li/a'))
    )



