from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json

URL = "https://my.anfcorp.com/psp/hr92pxt/?cmd=login"

schedule = "https://pshrprdext.anfcorp.com/psc/hr92pxt/EXTERNAL/HRMSEXT/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=AFHR_AF_STORE_TA1_FL&PanelCollapsible=Y&PTPPB_GROUPLET_ID=AF_STORE_TA1_FL&CRefName=AFHR_STORE_FL1"

data = {
        "timezoneOffset": "420",
        "ptmode": "f",
        "ptlangcd": "ENG",
        "ptinstalledlang": "GER,ENG,FRA,JPN,ZHS,POL,ITA,KOR,ESP,DUT",
        "userid": "02315004",
        "pwd": "2907981733"
        }

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",
                          chrome_options=options)

# Startup the Hollister page and login
driver.get(URL)
driver.find_element_by_id("userid").send_keys("02315004")
driver.find_element_by_id("pwd").send_keys("2907981733")
driver.find_element_by_class_name("ps-button").click()

# Go to schedule
driver.find_element_by_id("win0groupletPTNUI_LAND_REC_GROUPLET$5").click()


"""
with requests.Session() as session:
    post = session.post(URL, data=data)
    page = session.get(schedule)
    # print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all('table')
    for row in rows:
        print(row.get_text())
        """
