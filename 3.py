#!/usr/bin/python3
def isPrime(i):
	if i == 2: return 1
	if i < 3: return 0
	if i % 2 == 0: return 0
	j = 3
	while j*j <= i:
		if i % j == 0: return 0
		j += 2
	return 1

for i in range(775143,3,-2):
	if 600851475143%i==0:
		if isPrime(i):
			print(i)
			quit()

# 6857