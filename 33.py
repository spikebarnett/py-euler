#!/usr/bin/python3
def findDivisors(i):
	v=[]
	if (i < 2): return v
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

n=1
d=1
for i in range(1,10):
	for j in range(1,10):
		for s in range(1,10): # Shared digit
			if((i==s) or (j==s)): continue
			if(((i*10+s)/(s*10+j))==(i/j)):
				n*=(i*10+s);
				d*=(s*10+j);
print(int(d/gcd(n,d)))

# 100