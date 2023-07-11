from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    # link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    slog1 = browser.find_element(By.CSS_SELECTOR, "span#num1").text
    slog2 = browser.find_element(By.CSS_SELECTOR, "span#num2").text
    summ = int(slog1) + int(slog2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()