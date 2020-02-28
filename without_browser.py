from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

urlmca = 'http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do'

driver.get(urlmca)
search_btn = driver.find_element_by_id('imgSearchIcon')
search_btn.click()
time.sleep(5)
search_company_name_input = driver.find_element_by_id('searchcompanyname')
search_company_name_input.send_keys('Phoenix')
response = driver.execute_script('return fetchCINData()')

time.sleep(2)
table = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/section/div[4]/div[1]/div/table/tbody')
rows = table.find_elements_by_tag_name('tr')
print(len(rows))
for row in rows:
    cells = list(row.find_elements_by_tag_name('td'))
    print(cells[0].text)
