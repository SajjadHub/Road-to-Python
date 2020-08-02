from bs4 import BeautifulSoup
import requests
import json

URL = "https://my.anfcorp.com/psp/hr92pxt/?cmd=login"

schedule = "https://pshrprdext.anfcorp.com/psc/hr92pxt/EXTERNAL/HRMSEXT/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=AFHR_AF_STORE_TA1_FL&PanelCollapsible=Y&PTPPB_GROUPLET_ID=AF_STORE_TA1_FL&CRefName=AFHR_STORE_FL1"

data = {
        "userid": "02315004",
        "pwd": "2907981733"
        }

payload = {'data': json.dumps(data)}
with requests.Session() as session:
    post = session.post(URL, data=payload)
    page = session.get(schedule)
    print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows:
        print(row.get_text())
