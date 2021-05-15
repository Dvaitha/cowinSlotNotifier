from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/Dare/Downloads/chromedriver_win32/chromedriver.exe')# Path for chromedriver given in this repository
driver.get('https://www.cowin.gov.in/home')# Covin website
while(1==1):# infinite loop
    button= driver.find_element_by_class_name('status-switch')#to switch to search by district
    button.click()
    state=driver.find_element_by_id('mat-select-value-1')#select state dropdown
    state.click()
    select_state=driver.find_element_by_id('mat-option-11')#select state currently Gujarat
    select_state.click()
    time.sleep(2)
    district = driver.find_element_by_id('mat-select-value-3')# select district dropdown
    district.click()
    select_district = driver.find_element_by_id('mat-option-72')# select district currently selected is Surat Corporation
    select_district.click()
    search=driver.find_element_by_class_name('district-search')# search button click
    search.click()
    time.sleep(5)
    driver.refresh()