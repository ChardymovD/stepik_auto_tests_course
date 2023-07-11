from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    y = calc(x)


    answer = browser.find_element(By.CSS_SELECTOR, "#answer:required")
    answer.send_keys(y)
    time.sleep(3)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox:required")
    robot_checkbox.click()
    robot_radio = browser.find_element(By. CSS_SELECTOR, '#robotsRule[value="robots"]')
    robot_radio.click()
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

