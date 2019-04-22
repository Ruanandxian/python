from xml.parsers.expat import ParserCreate
from urllib import request
pp={}
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        if name=='yweather:location':
            pp['city']=attrs['city']
        if name=='yweather:condition' or name=='yweather:forecast':
            pp['forecast']=attrs
        #print('sax.start_element:%s,attrs:%s' % (name, str(attrs)))
    #def end_element(self):
        # pass
    #def char_data(self):
        # pass

def parseXML(xml_str):
    print(xml_str)
    parser=ParserCreate()
    handler=DefaultSaxHandler()
    parser.StartElementHandler=handler.start_element
    #parser.EndElementHandler=handle.end_element
    #parser.CharacterDataHandler=handle.char_data
    parser.Parse(xml_str)
    return {
        'city':pp['city'],
        'forecast':pp['forecast'],
    }

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL,timeout=4)as f:
    data=f.read()

result=parseXML(data.decode('utf-8'))
print(result)