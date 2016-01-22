__author__ = 'yubo'

import csv
import time

class Timer(object):
	def __init__(self, verbose=False):
		self.verbose = verbose

	def __enter__(self):
		self.start = time.time()
		return self

	def __exit__(self, *args):
		self.end = time.time()
		self.secs = self.end - self.start
		self.msecs = self.secs * 1000
		if self.verbose:
			print 'elapased time: %f ms' % self.msecs

def stat(file_name):
	reader = csv.reader(file(file_name, 'rb'))
	
	cnt = 0
	res = {}
	for line in reader:
		cnt += 1
		if cnt == 1:
			continue
	
		date = line[1].split(' ')[0]
		res[date] = res.get(date, 0) + 1

	return res

if __name__ == "__main__":
	with Timer(verbose=True) as t:
		res = stat('raitem.csv')


