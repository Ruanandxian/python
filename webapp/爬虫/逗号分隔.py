import csv
csvFile=open('D:/pycharm/webapp/爬虫/test.csv','w+')
try:
	writer=csv.writer(csvFile)
	writer.writerow(('number1','number2','number3'))
	for i in range(10):
		writer.writerow((i,i+2,i+3))
finally:
	csvFile.close()