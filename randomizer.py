import random
import csv

csv_file = open('spotify.csv')
reader = csv.reader(csv_file)

dump_file = open('dump.txt', 'w')

l =[]

for row in reader:
	l.append(row[0])
	

random.shuffle(l)

for row in l:
	print row
	dump_file.write('%s \n' % (row))