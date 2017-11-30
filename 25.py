#!/usr/bin/python3
f=1
s=1
c=f+s
ans=3


while(len(str(c)) < 1000):
	f=s
	s=c
	c=f+s
	ans+=1
print(ans)

# 4782