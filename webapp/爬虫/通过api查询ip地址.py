import json
from urllib.request import urlopen
def getadress(ip):
	response=urlopen('http://api.ipstack.com/'+ip+'?access_key=d65b8aa4d1fa4b2a4eac0780f2286a2c').read().decode('utf-8')
	responseJson=json.loads(response)
#	print(responseJson)
	return responseJson.get('country_code')

print(getadress('50.78.253.58'))