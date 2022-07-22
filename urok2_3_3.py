from selenium import webdriver
from selenium.webdriver.common.by import By
import math

# математическая функция от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

#Нажать на кнопку
button = browser.find_element(By.TAG_NAME, "button")
button.click()

#Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

#Считать значение для переменной x
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text  #Посчитать математическую функцию от x
y = calc(x)  #Посчитать математическую функцию от x
input1 = browser.find_element(By.CSS_SELECTOR, "#answer") #находим строку
input1.send_keys(y)  #Вставляем в строку результат функции

#Нажать на кнопку "Submit
button = browser.find_element(By.TAG_NAME, "button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()