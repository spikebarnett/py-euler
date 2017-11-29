#!/usr/bin/python3
def isPrime(n):
	if n<3:
		return 0
	if n%2==0:
		return 0
	i=3
	while i*i<=n:
		if n%i==0:
			return 0
		i+=2
	return 1

for i in range(775143,3,-2):
	if 600851475143%i==0:
		if isPrime(i):
			print(i)
			quit()

# 6857