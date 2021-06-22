import os
import time
import requests
from selenium import webdriver

driver = webdriver.Chrome('../driver/chromedriver')


url = 'https://netpeak.ua/'
driver.get(url)
print(url)
# assert requests.get(url).status_code == 200

url = driver.find_element_by_link_text("Карьера").get_attribute('href')
driver.get(url)
print(url)
# assert requests.get(url).status_code == 200

url = driver.find_element_by_link_text("Я хочу работать в Netpeak").get_attribute('href')
driver.get(url)
print(url)
# assert requests.get(url).status_code == 200

time.sleep(5)

driver.find_element_by_id("upload").send_keys('/home/marina/QA_netpeak/Резюме.png')

# driver.find_element_by_id("upload").click()
# driver.find_element_by_id("upload").send_keys(os.getcwd()+"/home/marina/Programming/SRC/Python/QA_netpeak/сrutches.png")


print(driver.find_element_by_xpath('//*[@id="up_file_name"]/label').text) #Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).

driver.find_element_by_id('inputName').click()
driver.find_element_by_id('inputName').send_keys("Марина")

driver.find_element_by_id('inputLastname').click()
driver.find_element_by_id('inputLastname').send_keys("Марина")

driver.find_element_by_id('inputEmail').click()
driver.find_element_by_id('inputEmail').send_keys("Test@test.com")

driver.find_element_by_name('by').click()
driver.find_element_by_name('by').send_keys('1999')

driver.find_element_by_name('bm').click()
driver.find_element_by_name('bm').send_keys('сентября')

driver.find_element_by_name('bd').click()
driver.find_element_by_name('bd').send_keys('9')

driver.find_element_by_id('inputPhone').click()
driver.find_element_by_id('inputPhone').send_keys("+380661112233")

driver.find_element_by_name('agree_rules').click()
driver.find_element_by_name('difficult').click()

color = driver.find_element_by_xpath('/html/body/div[2]/div/p').value_of_css_property('color')
red = "rgba(255, 0, 0, 1)"

if not red == color:
    raise Exception('Color not red')

url = driver.find_element_by_link_text("Курсы").get_attribute('href')
driver.get(url)
print(url)
