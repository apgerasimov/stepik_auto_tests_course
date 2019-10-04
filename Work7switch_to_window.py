from selenium import webdriver
import math

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

driver.get(link)
button = driver.find_element_by_css_selector('body > form > div > div > button').click()
#driver.switch_to.window('Redirect page')
first_window = driver.window_handles[0]
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
def calc(x):
   return str(math.log(abs(12 * math.sin(int(x)))))
x = driver.find_element_by_id('input_value')
x = x.text
y = calc(x)
answer = driver.find_element_by_id('answer').send_keys(y)
submit = driver.find_element_by_xpath('/html/body/form/div/div/button').click()
