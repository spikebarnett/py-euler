#!/usr/bin/python3
ones=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens=[0,0,6,6,5,5,5,7,6,6]

ans=0;
for i in range(1,1001):
	if(i%100<20):
		ans+=ones[i%100]
	else:
		ans+=ones[i%10]
		ans+=tens[int((i%100)/10)]
	if(i%1000>=100):
		if(i%100>0):
			ans+=10; # hundred and
			ans+=ones[int(i/100)%10];
	if(i%1000>=100):
		if(i%100==0):
			ans+=7; # hundred
			ans+=ones[int(i/100)%10];
	if(i==1000):
		ans+=11; # one thousand
print(ans)

# 21124