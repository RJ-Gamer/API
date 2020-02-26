from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

urlmca = 'http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do'

driver.get(urlmca)
search_btn = driver.find_element_by_id('imgSearchIcon')
search_btn.click()
search_company_name_input = driver.find_element_by_id('searchcompanyname')
search_company_name_input.send_keys('zapfin')
response = driver.execute_script('return fetchCINData()')
