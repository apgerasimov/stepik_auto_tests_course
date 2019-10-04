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
confirm_2 = driver.switch_to.alert
confirm_2 = confirm_2.text.split(': ')[-1] # выбираем только последнюю строку
pyperclip.copy(confirm_2) # копируем в буфер обмена последнюю строку из предидущего шага
confirm_2 = driver.switch_to.alert # снова переключаемся к алерту
confirm_2.accept() # закрываем его
driver.get('https://stepik.org/lesson/184253/step/4?unit=158843')
sign_up = driver.find_element_by_xpath('//*[@id="ember1505"]').click()
login = driver.find_element_by_xpath('//*[@id="id_login_email"]').send_keys('ap.gerasimov@gmail.com')
password = driver.find_element_by_xpath('//*[@id="id_login_password"]').send_keys('A123321123a')
login_button = driver.find_element_by_xpath('//*[@id="login_form"]/button').click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 800);")
time.sleep(2)
work_with_windows = driver.find_element_by_link_text('2.3 Работа с окнами').click()
my_task = driver.find_element_by_link_text('Задание: принимаем alert').click()
answer_field_stepik = driver.find_element_by_css_selector('textarea').send_keys(pyperclip.paste())  # вставляем ранее сохраненную строку в поле
driver.close()




