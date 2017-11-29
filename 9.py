#!/usr/bin/python3
for m in range(2,23):
	for n in range(1,m):
		a=m*m-n*n;
		b=2*m*n;
		c=m*m+n*n;
		if(a+b+c==1000):
			print(a*b*c)
			quit()