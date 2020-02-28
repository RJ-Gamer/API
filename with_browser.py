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

time.sleep(2)

table = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/section/div[4]/div[1]/div/table/tbody')
print(table)
rows = table.find_elements_by_tag_name('tr')


for index, row in enumerate(rows):
    cells = row.find_elements_by_tag_name('td')
    for cell in cells:
        print(cell.text)
