import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json

# Hollister login page
URL = "https://my.anfcorp.com/psp/hr92pxt/?cmd=login"

# Schedule page
schedule = "https://pshrprdext.anfcorp.com/psc/hr92pxt/EXTERNAL/HRMSEXT/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=AFHR_AF_STORE_TA1_FL&PanelCollapsible=Y&PTPPB_GROUPLET_ID=AF_STORE_TA1_FL&CRefName=AFHR_STORE_FL1"

# Data required for login
data = {
        "timezoneOffset": "420",
        "ptmode": "f",
        "ptlangcd": "ENG",
        "ptinstalledlang": "GER,ENG,FRA,JPN,ZHS,POL,ITA,KOR,ESP,DUT",
        "userid": "02315004",
        "pwd": "2907981733"
        }

# setting up selenium chrome
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')  # to show the browser
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",
                          chrome_options=options)

# Startup the Hollister page and login
driver.get(URL)
driver.find_element_by_id("userid").send_keys("02315004")
driver.find_element_by_id("pwd").send_keys("2907981733")
driver.find_element_by_class_name("ps-button").click()

# Go to schedule
driver.get(schedule)
# TODO: Get page source after dynamic elements are loaded in
# wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'gbAF_SCHED_CUR_VW$0')))
time.sleep(3)
# driver.refresh()
schedulePage = driver.execute_script("return document.documentElement.outerHTML")
tempfile = open("temp.html", "w")
tempfile.write(schedulePage)
tempfile.close()

print(driver.find_elements_by_id("divgbrAF_SCHED_CUR_VW$0"))

tempsoup = BeautifulSoup(schedulePage, "html5lib")
# print(tempsoup.find_all('tr'))
"""
rows = tempsoup.find_all('table')
for row in rows:
    print(row.get_text())
time.sleep(1)
"""
driver.quit()

"""
print("============================")
with requests.Session() as session:
    page = session.get(schedulePage)
    # print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all('table')
    for row in rows:
        print(row.get_text())
        """
