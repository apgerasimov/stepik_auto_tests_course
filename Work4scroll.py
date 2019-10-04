from selenium import webdriver
import math

driver = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
driver.get(link)
driver.implicitly_wait(3)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x = driver.find_element_by_id('input_value')
x = x.text
y = calc(x)
button = driver.find_element_by_css_selector('body > div > form > button')
driver.execute_script("window.scrollBy(0, 200);")
#driver.execute_script('return arguments[0].scrollIntoView;(true)', button)
answer = driver.find_element_by_id('answer')
answer.send_keys(y)
checkbox = driver.find_element_by_css_selector("[for='robotCheckbox']").click()
radio = driver.find_element_by_css_selector('#robotsRule').click()
button.click()


