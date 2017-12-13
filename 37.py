#!/usr/bin/python3
from array import array

def isPrime(i):
	if i == 2: return 1
	if i < 3: return 0
	if i % 2 == 0: return 0
	j = 3
	while j*j <= i:
		if i % j == 0: return 0
		j += 2
	return 1

def generatePrimes(i):
	p = []
	n = array('Q',[0 for j in range(i+1)])
	j = 2
	while (j<=i):
		if(n[j]==0):
			p.append(j);
			for k in range(j*j,i+1,j):
				n[k]=1
		j+=1
	return p

ans = 0
primes=generatePrimes(1000000)
for p in primes:
	if(p<10): continue
	i=str(p)
	while len(i) > 1:
		i=i[1:]
		if i[0]=="0": break
		if(isPrime(int(i))==0): break
		if len(i)==1:
			i=str(p)
			while len(i) > 1:
				i=i[:-1]
				if(isPrime(int(i))==0): break
				if len(i)==1:
					ans += p
					break
			break
print(ans)

# 748317
