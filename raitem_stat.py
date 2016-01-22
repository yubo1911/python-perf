__author__ = 'gzguoyubo'

import csv

reader = csv.reader(file('raitem.csv', 'rb'))

cnt = 0
res = {}
for line in reader:
	cnt += 1
	if cnt == 1:
		continue

	date = line[1].split(' ')[0]
	res[date] = res.get(date, 0) + 1

keys = res.keys()
keys.sort()
for k in keys:
	print k

print '='*16
for k in keys:
	print res[k]

