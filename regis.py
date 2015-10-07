import requests
import getpass
from bs4 import BeautifulSoup

def readWeb(url):
	req = requests.get(url)
	return req.text

usr = raw_input('input your id: ')
pw = getpass.getpass('password: ')
payload = {'form_username':usr,'form_password':pw,'zone':'0'}
#payload = {'form_username':'b5810500137','form_password':'Rain8bov','zone':'0'}
session = requests.Session()

memText = session.post('https://std.regis.ku.ac.th/_Login.php',data=payload)
soup = BeautifulSoup(memText.text,'lxml')

attr = {'id':'3'}
name = soup.find('tr',id='3')
name = name.find_all('td')[1].contents[0]
print "Welcome " + name + "."

attr = {'mode':'PRTKU2'}
regis = session.get('https://std.regis.ku.ac.th/_Student_RptKu.php?',params=attr)
soup = BeautifulSoup(regis.text,'lxml')
s = soup.find_all('table')
s = s[3]
s = s.find_all('tr')
for i in range(4,len(s)-5):
	print s[i].find_all('td')[2].contents[0]