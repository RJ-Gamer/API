from selenium import webdriver
import time
from selenium.webdriver.common.by import By

urlmca = 'http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do'

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.maximize_window()
driver.get(urlmca)

search_btn = driver.find_element_by_id('imgSearchIcon')
search_btn.click()
time.sleep(5)
search_company_name_input = driver.find_element_by_id('searchcompanyname')
search_company_name_input.send_keys('zapfin')
response = driver.execute_script('return fetchCINData()')
# table = driver.execute_script('showCINList()')
