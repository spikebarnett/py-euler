#!/usr/bin/python3

def isPrime(i):
	if i % 2 == 0: return 0
	j = 3
	while j*j <= i:
		if i % j == 0: return 0
		j += 1
	return 1

highest=0
aa = 0
bb = 0
for a in range(-999,1000):
	for b in range(-1000,1001):
		n = 0
		while isPrime(n*n + a*n + b)==1:
			n += 1
		if n > highest:
			highest = n
			aa = a
			bb = b
print(aa*bb)

# -59231