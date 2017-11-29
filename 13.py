#!/usr/bin/python3
with open("/home/cbarnett/git/py-euler/13.txt") as textFile:
	n = [int(line) for line in textFile]

ans=0
for i in n:
	ans+=i
print(str(ans)[0:10])

# 5537376230