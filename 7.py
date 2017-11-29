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

print(generatePrimes(1000000)[10000])

# 104743