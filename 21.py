#!/usr/bin/python3
def d(i):
	if (i < 2):
		return 0
	retval = 0;
	j=1
	while(j*j<=i):
		if (i % j == 0):
			retval += j;
			if (i/j != j):
				if (i/j != i):
					retval += (i/j);
		j+=1
	return retval

ans = 0
for i in range(2,10001):
	sum = d(i);
	if (i != sum):
		if (i == d(sum)):
			ans += i
print(ans)

# 31626