from bs4 import BeautifulSoup
import requests
import json

URL = 'https://cas.id.ubc.ca/ubc-cas/login?TARGET=https%3A%2F%2Fssc.adm.ubc.ca%2Fsscportal%2Fservlets%2FSRVSSCFramework'

scrape = 'https://courses.students.ubc.ca/cs/courseschedule?submit=Login&serviceType=courses&studentid=23401565'
course = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPEN&course=211'
cours1 = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=DSCI&course=100'

courseName = "CPEN"
courseCode = "211"
courseURL = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=' + str(courseName) + '&course=' + str(courseCode)

print(courseURL)

data = {
        "username": "salkaz26",
        "password": "Alkazzaz545217"
        }

payload = {'data': json.dumps(data)}
with requests.Session() as session:
    post = session.post(URL, data=payload)
    page = session.get(course)
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows:
        print(row.get_text())
