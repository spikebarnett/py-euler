#!/usr/bin/python3
p = [2,3,5,7,11,13,17,19]
f = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def getFactors(i):
	for j in p:
		n = 0
		while(i%j==0):
			i/=j
			n+=1
			if(n>f[j]):
				f[j]=n
		if(i==1):
			return

ans=1;
for i in range(2,21):
	getFactors(i)
for i in p:
	for j in range(0,f[i]):
		ans*=i;
print(ans)

# 232792560