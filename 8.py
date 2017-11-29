#!/usr/bin/python3
n = open('/home/cbarnett/git/py-euler/8.txt','r').read().replace('\n', '')
ans=0
for i in range(0,len(n)-4):
	ans=max(ans,int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4]))
print(ans)