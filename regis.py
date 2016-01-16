import requests
import getpass
from bs4 import BeautifulSoup

#login and welcome message
usr = raw_input('input your id: ')
pw = getpass.getpass('password: ')
payload = {'form_username':usr,'form_password':pw,'zone':'0'}
session = requests.Session()

memText = session.post('https://std.regis.ku.ac.th/_Login.php',data=payload)
soup = BeautifulSoup(memText.text,'lxml')

attr = {'id':'3'}
name = soup.find('tr',id='3')
name = name.findAll('td')[1].contents[0]
print "Welcome " + name + "."

#report
attr = {'mode':'PRTKU2'}
regis = session.get('https://std.regis.ku.ac.th/_Student_RptKu.php?',params=attr)
soup = BeautifulSoup(regis.text,'lxml')
s = soup.findAll('table')[3].findAll('table')[0]
s = s.findAll('tr')
for i in range(1,len(s)-1):
	ct = s[i].findAll('td')
	print ct[1].contents[0] + '\t' + ct[2].contents[0]

#_Student_Registration.php
headers = {'Referer': 'https://std.regis.ku.ac.th/_Student_Registration.php', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0'}
regis = session.get('https://std.regis.ku.ac.th/_Student_Registration.php',headers=headers)
soup = BeautifulSoup(regis.text,'lxml')
t = soup.findAll('td',class_='txt_add')[4]
t = t.findAll('input')
payload = {}
for i in t:
	payload[i['name']] = i['value']
code = raw_input('input subject code: ')
payload['Cs_Code'] = code

# =>inst_regis.php
headers['Referer'] = 'https://std.regis.ku.ac.th/inst_regis.php'
regis = session.post('https://std.regis.ku.ac.th/inst_regis.php',headers=headers,data=payload)
print regis.text

