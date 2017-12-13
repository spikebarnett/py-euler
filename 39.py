#!/usr/bin/python3
from array import array

def findDivisors(i):
	v=[]
	if (i < 2):
		v.append(1)
		return v
	j=1
	while j*j<=i:
		if (i % j == 0):
			v.append(j)
			if (i/j != j):
				v.append(i/j)
		j+=1
	return v

def gcd(n, d):
	divs=list(set(findDivisors(n)).intersection(findDivisors(d)))
	divs.sort()
	return divs[len(divs)-1]

o = array('Q',[0 for j in range(1001)])

for m in range(2,23):
	for n in range(1,m):
		if m%2==0 and n%2==0: continue
		if gcd(m,n) != 1: continue
		a = (m**2) - (n**2) 
		b = 2*m*n
		c = (m**2) + (n**2)
		p=a+b+c
		while p<=1000:
			o[p]+=1
			p+=a+b+c

ans=0
val=0
for i in range(0,len(o)):
	if o[i]>val:
		val=o[i]
		ans=i
print(ans)
	
# 840
