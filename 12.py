#!/usr/bin/python3
def numDevisors(i):
	retval=0
	j=1
	while(j*j<=i):
		if(i%j==0):
			retval+=2
			if(j*j==i):
				retval-=1
		j+=1
	return retval

n=1
m=1
while(numDevisors(n)<501):
	m+=1
	n+=m
print(n)

# 76576500