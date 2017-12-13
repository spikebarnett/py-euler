#!/usr/bin/python3
def isPandigital(s):
	#if len(s)!=9: return 0;
	digits = [0,0,0,0,0,0,0,0,0,0]
	for c in s: digits[int(c)]+=1
	if digits[0] >= 1: return 3
	for i in range(1,10):
		if digits[i] >= 2: return 2
		if digits[i] == 0: return 0
	return 1

ans = 0
for i in range(2,9999):
	n = str(i)
	for j in range(2,10):
		n += str(i*j)
		p = isPandigital(n)
		if p == 1:
			if int(n) > ans: ans = int(n)
			break
		if p >= 2:
			break
print(ans)

# 932718654
