from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    time.sleep(1)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    time.sleep(1)
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()