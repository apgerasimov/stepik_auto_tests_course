from selenium import webdriver
import math
driver = webdriver.Chrome()
link = ('http://suninjuly.github.io/get_attribute.html')

driver.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_value = driver.find_element_by_id('treasure')
x = x_value.get_attribute('valuex') # получаем атрибут "valuex"
y = calc(x)
answer = driver.find_element_by_id('answer')
answer.send_keys(y)
checkbox = driver.find_element_by_id("robotCheckbox")
checkbox.click()
radio = driver.find_element_by_id('robotsRule')
radio.click()
submit = driver.find_element_by_css_selector('body > div > form > div > div > button')
submit.click()
