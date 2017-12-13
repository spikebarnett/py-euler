#!/usr/bin/python3
def isPalindromic(a):
	for i in range(0,int(len(a)/2)):
		if(a[i]!=a[int(len(a)-i-1)]): return 0
	return 1

ans = 0
# 1 and 2 digit palindromes
for a in range(1,10,2):
	i = a
	if isPalindromic(bin(i)[2:])==1: ans += i
	i = a*10 + a
	if isPalindromic(bin(i)[2:])==1: ans += i
# 3 and 4 digit palindromes
for a in range(1,10,2):
	for b in range(0,10):
		i = a*100 + b*10 + a
		if isPalindromic(bin(i)[2:])==1: ans += i
		i = a*1000 + b*100 + b*10 + a
		if isPalindromic(bin(i)[2:])==1: ans += i
# 5 and 6 digit palindromes
for a in range(1,10,2):
	for b in range(0,10):
		for c in range(0,10):
			i = a*10000 + b*1000 + c*100 + b*10 + a
			if isPalindromic(bin(i)[2:])==1: ans += i
			i = a*100000 + b*10000 + c*1000 + c*100 + b*10 + a
			if isPalindromic(bin(i)[2:])==1: ans += i
print(ans)

# 872187
