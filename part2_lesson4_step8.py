from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "100")
    )
    book = browser.find_element(By.ID, "book")
    book.click()
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value").text
    y = calc(int(x))
    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(y)
    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()