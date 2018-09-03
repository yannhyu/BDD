from selenium import webdriver
from test.patly_homepage_driver import *

def before_scenario(context, scenario):
    browser = webdriver.Chrome()
    context.browser = PatlyHomepageDriver(browser)
    context.browser.go_to_homepage()
    context.mapping = {}

def after_scenario(context ,scenario):
    context.browser.quit()