from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from io import StringIO
html=urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
data=StringIO(html)
dudata=csv.reader(data)
for i in dudata:
    #print("the album \""+i[0]+"\" was released in "+str(i[1]))
    print(i)


'''url=urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
file=StringIO(url)
filename=csv.DictReader(file)
print(filename.fieldnames)
for row in filename:
    print(row)'''