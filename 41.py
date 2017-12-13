#!/usr/bin/python3
from itertools import permutations

def isPrime(i):
	if i == 2: return 1
	if i < 3: return 0
	if i % 2 == 0: return 0
	j = 3
	while j*j <= i:
		if i % j == 0: return 0
		j += 2
	return 1

perms = [''.join(p) for p in permutations('7654321')]
perms.sort

for p in perms:
	if isPrime(int(p))==1:
		print(p)
		break

# 7652413