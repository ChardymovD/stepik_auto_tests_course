
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    y = calc(int(x))

    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox:required")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()