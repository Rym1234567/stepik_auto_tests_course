from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button1 = browser.find_element(By.ID, "book")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button1.click()
browser.execute_script("window.scrollBy(0, 100);")
x = browser.find_element(By.ID, "input_value").text
field = browser.find_element(By.TAG_NAME, "input")
field.send_keys(str(calc(int(x))))
button2 = browser.find_element(By.ID, "solve")
button2.click()
time.sleep(10)
browser.quit()

