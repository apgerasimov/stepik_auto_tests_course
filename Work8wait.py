from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

driver.get(link)
price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100")) # ожидаем пока текст поля станет равным $100
book_button = driver.find_element_by_id('book').click() # кликаем по кнопке
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x = driver.find_element_by_id('input_value')
x = x.text
y = calc(x)
answer = driver.find_element_by_id('answer').send_keys(y)
submit = driver.find_element_by_id('solve').click()
