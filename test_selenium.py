# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:03:03 2024

@author: L
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#options = ChromeOptions()
#options.add_argument('headless') #for headless
#options.add_argument('disable-gpu')
#driver = Chrome(chrome_options=options)


option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
chromedriver_path = r"c:\HP\chrome-win64\chrome.exe"

cService = webdriver.ChromeService(chromedriver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

driver.get("https://mbasic.facebook.com/Central.Intelligence.Agency")
time.sleep(3)

email_elem = driver.find_element(By.ID, "email")  # Locate by ID
email_elem.send_keys("-")
time.sleep(2)
password_elem = driver.find_element(By.ID, "pass")  # Locate by ID
password_elem.send_keys("-")
time.sleep(2)
submit_elem = driver.find_element(By.ID,"loginbutton")
submit_elem.click()
driver.get("https://mbasic.facebook.com/Central.Intelligence.Agency")
time.sleep(3)
    # comment 100 times
for i in range(2):
    time.sleep(3)
    commentBox = driver.find_element(By.ID,"composerInput")
    commentBox.send_keys("https://wirelessbci.cloud")
    time.sleep(1)
    sendButton = driver.find_element(By.TAG_NAME, "button")[0] 
    sendButton.click()