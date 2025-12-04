# MATBUDSJETT script

# https://messages.google.com/web/conversations/CgjICeSvgS_qfxICMTQ --DNB message log

from selenium import webdriver
from selenium.webdriver.common.by import By


endpoint = "https://messages.google.com/web/conversations/CgjICeSvgS_qfxICMTQ"
driver = webdriver.Chrome()
driver.get(endpoint)

elements = driver.find_elements(By.CLASS_NAME, "ng-star-inserted") #maybe select the chat befor as this seemed to grab everything
btn_sign_in = driver.find_element(By.CLASS_NAME, "mat-mdc-button-ripple")
btn_sign_in = driver.find_element(By.CLASS_NAME, "mdc-button__label")
print(elements)
