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
# print(rows[5].text)
for index, row in enumerate(rows):
    cells = list(row.find_elements_by_tag_name('td'))
    print("[{0}] -- {1}".format(index+1, cells[0].text))


company_choice = int(input("Enter the number beetween 1 and {0} \n".format(len(rows))))
company = list((rows[company_choice-1].text).split(' '))
com = ''
for strng in company[:-1]:
    com = com + strng + " "

print("You selected : {0}".format(com))
