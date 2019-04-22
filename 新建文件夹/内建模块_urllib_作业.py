from urllib import request
import ssl
import json
def fetch_data(url):
#    with request.urlopen(url,context=ssl._create_unverified_context()) as m:
#        data=m.read()
#        return json.loads(data)
    with request.urlopen(url,context=ssl._create_unverified_context()) as f:
        c=json.load(f)
    return c



URL='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data=fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city']=='Beijing'
print('ok')