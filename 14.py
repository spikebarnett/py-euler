#!/usr/bin/python3
def collatz(i):
	retval=1
	while(i!=1):
		if(i%2==0):
			i/=2
		else:
			i=(i*3)+1
		retval+=1
	return retval

ans=0
chain=0
for i in range(1,1000000):
	tmp=collatz(i)
	if(tmp>chain):
		chain=tmp
		ans=i
print(ans)

# 837799