from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher('re')

@when('I go to new online services')
def step_imp(context):
    link = context.browser.find_element(By.XPATH, '//*[@id="first-navbar"]/ul/li[4]/a').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div[2]/div/div/div/div[1]/div[1]')
    action = ActionChains(context.browser)
    action.move_to_element(link)
    link2 = context.browser.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div[2]/div/div/div/div[2]/div[3]/a')
    action.move_to_element(link2).click().perform()
    link = context.browser.find_element(By.XPATH, '//*[@id="find"]').click()
    link = context.browser.find_element(By.XPATH, '//*[@id="videoModal"]/div/div/div/button/span').click()
    word = 'Позвонить на ЛПО'
    good_word = word.encode('cp1251').decode('utf8')
    link = context.browser.find_element(By.LINK_TEXT, good_word).click()

    def test_function():
        text = "+7(495)6300000"
        link = context.browser.find_element(By.XPATH, '//*[@id="telModal"]/div/div/div/h3').text
        assert (text == link)
    test_function()
    actions = ActionChains(context.browser)
    actions.send_keys(Keys.ESCAPE).perform()

    link = context.browser.find_element(By.XPATH, '//*[@id="tab-a-form"]').click()
    time.sleep(3)
    form1 = context.browser.find_element(By.XPATH, '//*[@id="Login"]').send_keys('anichkin@upt24.ru')
    form2 = context.browser.find_element(By.XPATH, '//*[@id="Password"]').send_keys('1234567')
    link = context.browser.find_element(By.XPATH, '//*[@id="authbtn"]').click()
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, '//*[@id="tab-a-form"]'))
    )
    link = context.browser.find_element(By.XPATH, '//*[@id="tab-a-form"]').click()
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="notification-deadline-wrapper"]/div/div/div/div[3]/div/div/a'))
    )
    element.click()

    time.sleep(20)

