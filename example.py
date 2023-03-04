
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://internet-cabinet.ru/habarovsk/zhivotnyje-uu/koshki-uu/")
(driver.find_elements(
    By.XPATH, "//*[@class=\"it-img\"]"))[1].click()

sleep(2)
driver.save_screenshot('pet_home.png') 

driver.quit()
