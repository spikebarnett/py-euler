#!/usr/bin/python3

fact = [1,1,2,6,24,120,720,5040,40320,362880]

t=0;
for i in range(10,99999):
	s=0
	n=i
	while(int(n)>0):
		s+=fact[int(n%10)]
		n/=10
	if(i==s): t+=i

print(t)

# 40730
