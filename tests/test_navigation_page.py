import os
import time
import requests
from selenium import webdriver



def go_to_home_page():
    url = 'https://netpeak.ua/'
    driver.get(url)
    print(url)
    assert requests.get(url).status_code == 200