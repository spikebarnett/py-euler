#!/usr/bin/python3
import array

def generatePrimes(i):
	p = []
	n = array.array('Q',[0 for j in range(i+1)])
	j = 2
	while (j<=i):
		if(n[j]==0):
			p.append(j);
			for k in range(j*j,i+1,j):
				n[k]=1
		j+=1
	return p

def isPrime(i):
	if i < 3: return 0
	if i % 2 == 0: return 0
	j = 3
	while j*j <= i:
		if i % j == 0: return 0
		j += 2
	return 1

primes=generatePrimes(999)
highest=0
aa = 0
bb = 0
for a in range(-999,999):
	for b in primes:
		n = 0
		while isPrime(n*n + a*n + b)==1:
			n += 1
		if n > highest:
			highest = n
			aa = a
			bb = b
print(aa*bb)

# -59231
