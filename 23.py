#!/usr/bin/python3
def DivisorsSum(i):
	if (i < 2):
		return 0
	retval = 0
	j=1
	while(j*j<=i):
		if (i % j == 0):
			retval += j
			if(i/j != j):
				if(i/j != i):
					retval += int(i/j)
		j+=1
	return retval

abundants = []
abundant_sums = []
for i in range(0,28124):
	if (i < DivisorsSum(i)):
		abundants.append(i)
for i in range(0, int(len(abundants)/2)):
	for j in range(i, len(abundants)):
		if (abundants[i] + abundants[j] < 28124):
			abundant_sums.append(abundants[i]+abundants[j])

abundant_sums.sort()
abundant_sums=set(abundant_sums)

ans = 0
for i in range(1, 28124):
	if not(i in abundant_sums):
		ans += i;
print(ans)

# 4179871