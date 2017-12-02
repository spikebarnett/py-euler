#!/usr/bin/python3

ans = -1 # Setting to -1 so as to not count 1;
for a in range(0,10):
	for b in range(0,10):
		for c in range(0,10):
			for d in range(0,10):
				for e in range(0,10):
					for f in range(0,10):
						p = a**5 + b**5 + c**5 + d**5 + e**5 + f**5;
						n = a + b*10 + c*100 + d*1000 + e*10000 + f*100000;
						if (p == n): ans += p;
print(ans)

# 443839
