#!/usr/bin/python3
from pprint import pprint

def isPandigital(s):
	if len(s)!=9: return 0;
	digits = [0,0,0,0,0,0,0,0,0,0]
	for c in s:
		digits[int(c)]+=1
	for i in range(1,10):
		if digits[i] != 1: return 0
	return 1

prods=[]
for a in range(2,9877):
	for b in range(2,99):
		c=a*b
		d=str(a)+str(b)+str(c)
		if isPandigital(d)==1:
			prods.append(c)
prods=list(set(prods))
prods.sort()
ans = 0
for i in prods:
	ans+=i
print(ans)

# 45228