from selenium import webdriver
import os

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

driver.get(link)
first_name = driver.find_element_by_name('firstname')
last_name = driver.find_element_by_name('lastname')
email = driver.find_element_by_name('email')
first_name.send_keys('Andrew')
last_name.send_keys('Ivanov')
email.send_keys('ivanov@gmail.com')
download_file = driver.find_element_by_id('file')
file = os.path.join('C:/Users/qa/Desktop/ggg.txt') # прописываем путь к файлу
download_file.send_keys(file) # загружаем файл
submit = driver.find_element_by_xpath('/html/body/div/form/button').click()