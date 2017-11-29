#!/usr/bin/python3
cache=[[0]*21 for i in range(21)]
cache[0][0]=1;

def move(x,y):
	if(cache[x][y]!=0):
		return cache[x][y]
	if(cache[y][x]!=0):
		return cache[y][x]
	retval=0
	if(x>0):
		retval+=move(x-1,y);
	if(y>0):
		retval+=move(x,y-1);
	return retval

for x in range(0,21):
	for y in range(0,21):
		cache[x][y]=move(x,y);
print(move(20,20))

# 137846528820