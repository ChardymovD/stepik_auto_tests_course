from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    y = calc(int(x))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

