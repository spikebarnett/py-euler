#!/usr/bin/python3
def checkFactors(i):
	for j in range(101,999):
		if(i%j==0):
			if(i/j>99):
				if(i/j<1000):
					return i;
	return 0;

for a in range(9,-1,-1):
	for b in range(9,-1,-1):
		for c in range(9,-1,-1):
			ans=(a*100000 + b*10000 + c*1000 + c*100 + b*10 + a)
			if(checkFactors(ans)!=0):
				print(ans)
				quit()