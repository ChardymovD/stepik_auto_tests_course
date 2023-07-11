from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']:required")
    first_name.send_keys("Dmitriy")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']:required")
    last_name.send_keys("Sergeevich")
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']:required")
    email.send_keys("test@test.com")
    send_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "part2_lesson2_step8.txt")
    send_file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
