import csv

peoples = [
	{'name':'Маша', 'age':'25', 'job':'Scientist'},
	{'name':'Вася', 'age':'8', 'job':'Programmer'},
	{'name':'Эдуард', 'age':'48', 'job':'Big boss'}
	]

with open ('peoples.csv','w',encoding = 'utf-8') as f:
	fields = ['name','age','job']
	writer = csv.DictWriter(f,fields,delimiter = ';')
	for people in peoples:
		writer.writerow(people)