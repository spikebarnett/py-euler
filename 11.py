#!/usr/bin/python3
with open("/home/cbarnett/git/py-euler/11.txt") as textFile:
	n = [line.split() for line in textFile]

for x in range(0,20):
	for y in range(0,20):
		n[x][y]=int(n[x][y])

ans=0
for x in range(0,20):
	for y in range(0,20):
		if(x<17):
			ans=max(ans,n[x][y]*n[x+1][y]*n[x+2][y]*n[x+3][y]);
		if(y<17):
			ans=max(ans,n[x][y]*n[x][y+1]*n[x][y+2]*n[x][y+3]);
			if(x<17):
				ans=max(ans,n[x][y]*n[x+1][y+1]*n[x+2][y+2]*n[x+3][y+3]);
				ans=max(ans,n[x][y+3]*n[x+1][y+2]*n[x+2][y+1]*n[x+3][y]);
print(ans)

# 70600674