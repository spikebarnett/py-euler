#!/usr/bin/python3
import itertools
perm = list(itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
ans = ""
for c in perm[999999]:
	ans += c
print(ans)
# 4179871