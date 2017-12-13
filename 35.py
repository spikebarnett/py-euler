#!/usr/bin/python3
import array

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
	n = array.array('Q',[0 for j in range(i+1)])
	j = 2
	while (j<=i):
		if(n[j]==0):
			p.append(j);
			for k in range(j*j,i+1,j):
				n[k]=1
		j+=1
	return p

def rotate(i):
	if i < 10: return i
	j = i % 10
	i /= 10
	return int(str(int(j))+str(int(i)))

ans = 0
primes = generatePrimes(1000000)
for i in primes:
	j = rotate(i)
	while 1==1:
		if j == i:
			ans += 1
			break
		if isPrime(j)==1: j=rotate(j)
		else: break
print(ans)

# 55