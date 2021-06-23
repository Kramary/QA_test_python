import os
import time
import requests
from selenium import webdriver



def test_courses():
    url = driver.find_element_by_link_text("Курсы").get_attribute('href')
    driver.get(url)
    assert requests.get(url).status_code == 200