#!/usr/bin/python3
import csv

def nameValue(s):
	retval = 0
	for i in range(0,len(s)):
		retval += ord(s[i])-96
	return retval;

names = []
with open('/home/cbarnett/git/py-euler/names.txt') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			for name in row:
				names.append(name.lower())

names.sort()
ans = 0;
for name in range(0,len(names)):
	ans += (nameValue(names[name]) * (name+1))
print(ans)

# 871198282