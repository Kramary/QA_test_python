import os
import time
import requests
from selenium import webdriver

driver = webdriver.Chrome('../driver/chromedriver')

def go_to_home_page():
    url = 'https://netpeak.ua/'
    driver.get(url)
    print(url)
    assert requests.get(url).status_code == 200

def test_career_page():
    url = driver.find_element_by_link_text("Карьера").get_attribute('href')
    driver.get(url)
    print(url)
    assert requests.get(url).status_code == 200

def test_app_form():
    url = driver.find_element_by_link_text("Я хочу работать в Netpeak").get_attribute('href')
    driver.get(url)
    print(url)
    assert requests.get(url).status_code == 200

def test_fail_CV():
    driver.find_element_by_id("upload").send_keys('/home/marina/QA_netpeak/Резюме.png')
    answer = driver.find_element_by_xpath('//*[@id="up_file_name"]/label').text
    reference = "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."
    #if not answer == reference:
        #raise Exception("CV error didn't work")

def test_fill_name():
    send = "Марина"
    driver.find_element_by_id('inputName').click()
    driver.find_element_by_id('inputName').send_keys(send)

def test_fill_last_name():
    send = "Марина"
    driver.find_element_by_id('inputLastname').click()
    driver.find_element_by_id('inputLastname').send_keys(send)

def test_fill_email():
    send = "Test@test.com"
    driver.find_element_by_id('inputEmail').click()
    driver.find_element_by_id('inputEmail').send_keys(send)

def test_fill_birth_year():
    driver.find_element_by_name('by').click()
    driver.find_element_by_name('by').send_keys('1999')

def test_fill_birth_month():
    driver.find_element_by_name('bm').click()
    driver.find_element_by_name('bm').send_keys('сентября')

def test_fill_birth_day():
    driver.find_element_by_name('bd').click()
    driver.find_element_by_name('bd').send_keys('9')

def test_writing_phone():
    driver.find_element_by_id('inputPhone').click()
    driver.find_element_by_id('inputPhone').send_keys("+380661112233")

def test_sand_form():
    driver.find_element_by_name('agree_rules').click()
    driver.find_element_by_name('difficult').click()

def test_check_color():
    color = driver.find_element_by_xpath('/html/body/div[2]/div/p').value_of_css_property('color')
    red = "rgba(255, 0, 0, 1)"
    if not red == color:
        raise Exception('Color not red')

def test_courses():
    url = driver.find_element_by_link_text("Курсы").get_attribute('href')
    driver.get(url)
    assert requests.get(url).status_code == 200
    assert url == "https://school.netpeak.group/"
    driver.close()