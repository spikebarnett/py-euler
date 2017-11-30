#!/usr/bin/python3
import datetime

ans=0
for y in range(1,101):
	for m in range(1,13):
		if(datetime.date(1900+y, m, 1).weekday()==6):
			ans+=1
print(ans)

# 171