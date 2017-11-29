#!/usr/bin/python3
f = 1
s = 2
c = 0
ans = 0
while c < 4000000:
	if s%2==0:
		ans += s
	c = f + s
	f = s
	s = c
print (ans)

# 4613732