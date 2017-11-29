#!/usr/bin/python3
ans = 0;
for x in range(3, 1000,3):
	ans += x
for x in range(5, 1000,5):
	ans += x
for x in range(15, 1000,15):
	ans -= x
print(ans)

# 233168