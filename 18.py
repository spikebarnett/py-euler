#!/usr/bin/python3
with open("/home/cbarnett/git/py-euler/18.txt") as textFile:
	tri = [line.split() for line in textFile]
tri = [[int(y) for y in x] for x in tri]
cache=[[0]*16 for i in range(16)]

def sum(r,p):
	if(cache[r][p]!=0):
		return cache[r][p]
	if(r==14):
		return tri[r][p]
	return tri[r][p]+max(sum(r+1,p),sum(r+1,p+1))

for r in range(14,-1,-1):
	for p in range(0,r+1):
		cache[r][p]=sum(r,p)
print(sum(0,0))

# 1074