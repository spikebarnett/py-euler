#!/usr/bin/python3
import re
import decimal

r = re.compile(r'.+?(.+?)\1{4}')

def repeatPeriod(s):
	result = r.match(s)
	if result != None:
		return len(result.group(1))
	else:
		return 0

ans=0
highest=0
decimal.getcontext().prec = 5000
for i in range(980,1000):
	j=str(decimal.Decimal(1)/decimal.Decimal(i))
	tmp = repeatPeriod(j)
	if tmp > highest:
		highest = tmp
		ans = i
print(ans)

# 983