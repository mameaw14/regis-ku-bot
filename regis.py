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
