#Module 2 ex.4 part 2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

path = 'C:\Selenium\chromedriver.exe'
browser = webdriver.Chrome(path)

browser.get('http://suninjuly.github.io/explicit_wait2.html')

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'10000'))
browser.find_element_by_id("book").click()

x = calc(int(browser.find_element_by_id('input_value').text))

input3 = browser.find_element_by_css_selector('#answer')
input3.send_keys(x)

button = browser.find_element_by_id('solve')
button.click()

alert = browser.switch_to.alert
print(alert.text)
alert.accept()

browser.close()
browser.quit()