import time

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

use_step_matcher('re')


@when('I wait to agreement button')
def step_impl(context):
    element = WebDriverWait(context.browser, 5).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#Agree"))
    )






