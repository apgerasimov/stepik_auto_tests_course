from selenium import webdriver
import math
driver = webdriver.Chrome()
link = ('http://suninjuly.github.io/math.html')

driver.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x = driver.find_element_by_css_selector('#input_value')
x = x.text # считываем значение х со страницы
y = calc(x)
answer = driver.find_element_by_css_selector('#answer')
answer.send_keys(y)
checkbox = driver.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()
people_radio = driver.find_element_by_id("peopleRule") #
people_checked = people_radio.get_attribute("checked") # Находим атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение
print("value of people radio: ", people_checked) # выводим "value of people radio"  проверяем что оно отмечено по умолчанию
assert people_checked == "true", "People radio is not selected by default"
radio = driver.find_element_by_id('robotsRule')
robots_checked = radio.get_attribute("checked")
assert robots_checked is None
radio.click()
submit = driver.find_element_by_css_selector('body > div > form > button')
submit.click()
