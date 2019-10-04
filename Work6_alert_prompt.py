from selenium import webdriver
import math
import pyperclip # пакет для сохранения в буфер обмена
import time

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
driver.implicitly_wait(7)

driver.get(link)
button = driver.find_element_by_css_selector('body > form > div > div > button').click()
confirm = driver.switch_to.alert
confirm.accept()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x = driver.find_element_by_id('input_value')
x = x.text
y = calc(x)
answer_field = driver.find_element_by_id('answer').send_keys(y)
submit = driver.find_element_by_css_selector('body > form > div > div > button').click()





