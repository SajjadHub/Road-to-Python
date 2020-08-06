from bs4 import BeautifulSoup
import requests
import json
import os

# URL to SSC login page
URL = 'https://cas.id.ubc.ca/ubc-cas/login?TARGET=https%3A%2F%2Fssc.adm.ubc.ca%2Fsscportal%2Fservlets%2FSRVSSCFramework'


# Taking in course information
courseName = input("Please enter a course name:\n")
courseCode = input("Please enter a course code:\n")

# Contructing course url
courseURL = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=' + str(courseName) + '&course=' + str(courseCode)

# print(courseURL)
print("=========\n")

# Login data for login form
data = {
        "username": os.getenv('username'),
        "password": os.getenv('password')
        }

# Preparing login data
payload = {'data': json.dumps(data)}

# Start a session
with requests.Session() as session:
    # Login
    post = session.post(URL, data=payload)

    # Go to course url
    page = session.get(courseURL)

    # Get and parse data
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.find_all('tr', class_='section1')
    rows += (soup.find_all('tr', class_='section2'))
    for row in rows:
        print(row.find('td').contents[0])
